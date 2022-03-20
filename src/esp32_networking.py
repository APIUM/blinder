import network
from config import Config


class Network:
    def __init__(self, config: Config):
        self.config = config
        self.sta_if = network.WLAN(network.STA_IF)

    def list_networks(self):
        print("Looking for networks...")
        networks = self.sta_if.scan()
        print("Found networks:")
        print("---------")
        for net in networks:
            print(net)

    def connect(self):
        print("Connecting to wifi SSID [%s]" % self.config.WIFI_SSID)
        if not self.sta_if.isconnected():
            print("Connecting to network...")
            self.sta_if.active(True)
            self.sta_if.connect(self.config.WIFI_SSID, self.config.WIFI_PASSWORD)
            while not self.sta_if.isconnected():
                pass
        print("Network config:", self.sta_if.ifconfig())

    def disconnect(self):
        self.sta_if.disconnect()
