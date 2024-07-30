from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent a silver service taxi object."""

    def __init__(self, name, fuel, fanciness=4):
        """Initialise a silver service taxi, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness
        self.flag_fall = 4.50

    def __str__(self):
        """Return a string like a Taxi but with flag fall and total fare."""
        return (f'{super().__str__()} plus flagfall of ${self.flag_fall:.2f}, '
                f'fare = ${self.price_per_km * self._odometer + self.flag_fall:.2f}')
