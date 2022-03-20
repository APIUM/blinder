import stepper

class Blinder:
    """Run the blind controller."""
    def __init__(self, step, dir, en, rst):
        self.open = False
        self.stepper = stepper.Stepper(step, dir, en, rst)

    def open(self):
        """Open the blinds."""
        self.stepper.revolution(10)

    def close(self):
        """close the blinds."""
        self.stepper.revolution(-10)