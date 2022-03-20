from esp32_networking import Network
from config import Config
import mqtt_as
import machine
import uasyncio
import blinder


def mqtt_callback(topic, msg, retained):
    print((topic, msg, retained))
    callback_list.append(MqttMessage(topic, msg))


topic_list = [
    "blinder/open",
    "blinder/close",
    "blinder/reset",
    "blinder/enable",
    "blinder/disable"
]


async def mqtt_conn_han(client):
    for topic in topic_list:
        await client.subscribe(topic, 1)


callback_list = []


class MqttMessage:
    def __init__(self, topic, data):
        self.TOPIC = topic.decode("utf-8")
        self.DATA = data.decode("utf-8")

    def get(self):
        return self.TOPIC, self.DATA


async def main():
    # Get configuration
    config = Config()

    # Blind and system config
    blinds = blinder.Blinder(
        step=Config.PIN_STEP,
        dir=Config.PIN_DIR,
        en=Config.PIN_EN,
        rst=Config.PIN_RESET
    )
    net = Network(config)

    # MQTT Config
    mqtt_as.config["subs_cb"] = mqtt_callback
    mqtt_as.config["connect_coro"] = mqtt_conn_han
    mqtt_as.config["server"] = config.MQTT_BROKER_URL
    mqtt_as.MQTTClient.DEBUG = True  # Optional: print diagnostic messages

    net.connect()

    client = mqtt_as.MQTTClient(mqtt_as.config)
    try:
        await client.connect()

        while True:
            if callback_list:
                callback = callback_list.pop()
                print("Processing callback...")
                if callback.TOPIC in "blinder/open":
                    print("Open blinds callback")
                    blinds.open()
                elif callback.TOPIC in "blinder/close":
                    print("Close blinds callback")
                    blinds.close()
                elif callback.TOPIC in "blinder/reset":
                    print("Reset blinds callback")
                    blinds.reset()
                elif callback.TOPIC in "blinder/enable":
                    print("Enable blinds callback")
                    blinds.enable()
                elif callback.TOPIC in "blinder/disable":
                    print("Disable blinds callback")
                    blinds.disable()
                else:
                    print("No match for topic")
                    print(callback.TOPIC)
                    print(callback.DATA)
            else:
                await uasyncio.sleep(1)

    finally:
        client.close()  # Prevent LmacRxBlk:1 errors


uasyncio.run(main())
