from prac_09.car import Car


class UnreliableCar(Car):
    """Represent an unreliable car object."""
    def __init__(self, name, fuel, reliability):
        """Initialise an unreliable car, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability
