CURRENT_YEAR = 2022


class Guitar:

    def __init__(self, name="", year=0, cost=0.0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        """Get guitar's age"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """determine if guitar is vintage"""
        return self.get_age() >= 50

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}\n"
