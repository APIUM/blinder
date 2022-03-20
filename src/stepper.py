"""Micropython module for stepper motor driven by Easy Driver."""
from machine import Pin
from time import sleep, sleep_us


class Stepper:
    """Class for stepper motor driven with DRV8825."""

    def __init__(self, step_pin, dir_pin, enable_pin, reset_pin):
        """Initialise stepper."""
        self.stp = step_pin
        self.dir = dir_pin
        self.en = enable_pin
        self.rst = reset_pin

        self.stp.init(Pin.OUT)
        self.dir.init(Pin.OUT)
        self.en.init(Pin.OUT)
        self.rst.init(Pin.OUT)

        self.step_time = 20  # us
        self.steps_per_rev = 1600
        self.current_position = 0

    def enable(self):
        """Power on stepper."""
        self.en.value(1)

    def disable(self):
        """Power off stepper."""
        self.en.value(0)
        self.current_position = 0
    
    def reset(self):
        """Reset driver."""
        self.rst.value(1)
        sleep(1)
        self.rst.value(0)

    def steps(self, step_count):
        """Rotate stepper for given steps."""
        self.dir.value(0 if step_count > 0 else 1)
        for i in range(abs(step_count)):
            self.stp.value(1)
            sleep_us(self.step_time)
            self.stp.value(0)
            sleep_us(self.step_time)
        self.current_position += step_count

    def rel_angle(self, angle):
        """Rotate stepper for given relative angle."""
        steps = int(angle / 360 * self.steps_per_rev)
        self.steps(steps)

    def abs_angle(self, angle):
        """Rotate stepper for given absolute angle since last power on."""
        steps = int(angle / 360 * self.steps_per_rev)
        steps -= self.current_position % self.steps_per_rev
        self.steps(steps)

    def revolution(self, rev_count):
        """Perform given number of full revolutions."""
        self.steps(rev_count * self.steps_per_rev)

    def set_step_time(self, us):
        """Set time in microseconds between each step."""
        if us < 20:  # 20 us is the shortest possible for esp8266
            self.step_time = 20
        else:
            self.step_time = us