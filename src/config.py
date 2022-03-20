from micropython import const

class Config:
    # ** NETWORK CONFIGURATION ** #
    WIFI_SSID = ""
    WIFI_PASSWORD = ""
    MQTT_BROKER_URL = ""

    # ** PIN DEFINITIONS ** #
    # Step Pin
    PIN_STEP = const(19)
    # Direction pin
    PIN_DIR = const(23)
    # Enable Pin
    PIN_EN = const(22)
    # Reset Pin
    PIN_RESET = const(21)

