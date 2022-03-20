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
    "blinder/close"
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

    # Pin definitions
    i2c_scl_pin = machine.Pin(config.PIN_I2C_SCL)
    i2c_sda_pin = machine.Pin(config.PIN_I2C_SDA)

    # Blind and system config
    i2c = machine.SoftI2C(scl=i2c_scl_pin, sda=i2c_sda_pin, freq=400_000)
    blinds = blinder.Blinder(i2c)
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
                    print("Open blinders callback")
                    await blinds.open()
                elif callback.TOPIC in "blinder/close":
                    print("Close blinds callback")
                    await blinds.close()
                else:
                    print("No match for topic")
                    print(callback.TOPIC)
                    print(callback.DATA)
            else:
                await uasyncio.sleep(1)

    finally:
        door.stop()
        client.close()  # Prevent LmacRxBlk:1 errors


uasyncio.run(main())
