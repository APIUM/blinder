from micropython import const

class Config:
    # ** NETWORK CONFIGURATION ** #
    WIFI_SSID = ""
    WIFI_PASSWORD = ""
    MQTT_BROKER_URL = ""

    # ** STEPPER CONFIG ** #
    STEP_TIME_US = 100
    STEPS_PER_REV = 1600

    # ** PIN DEFINITIONS ** #
    # Step Pin
    PIN_STEP = const(19)
    # Direction pin
    PIN_DIR = const(23)
    # Enable Pin
    PIN_EN = const(22)
    # Reset Pin
    PIN_RESET = const(21)
