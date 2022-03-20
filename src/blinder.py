import stepper

class Blinder:
    """Run the blind controller."""
    def __init__(self, step, dir, en, rst):
        self.stepper = stepper.Stepper(step, dir, en, rst)
        self.stepper.reset()
        self.stepper.enable()

    def __del__(self):
        """Disable stepper on destroy."""
        self.stepper.disable()

    def open(self):
        """Open the blinds."""
        print("Opening...")
        self.stepper.revolution(10)

    def close(self):
        """Close the blinds."""
        print("Closing...")
        self.stepper.revolution(-10)

    def reset(self):
        """Close the blinds."""
        print("Reseting...")
        self.stepper.reset()

    def enable(self):
        """Enable stepper."""
        print("Enabling...")
        self.stepper.enable()

    def disable(self):
        """Disable stepper."""
        print("Disabling...")
        self.stepper.disable()