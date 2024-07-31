from prac_09.musician import Musician


class Band(Musician):
    """Represents a band object."""

    def __init__(self, band_name):
        """Initialise a band, based on parent class Musician."""
        super().__init__()
        self.band_name = band_name
        self.band_info = ''
        self.band_lists = []

    def add(self, band_team):
        """Add a band to the information."""
        self.name = band_team.name
        self.band_lists.append(band_team)
        if self.band_info == '':
            self.band_info = Musician.__str__(band_team)
        else:
            self.band_info += ', ' + Musician.__str__(band_team)

    def __str__(self):
        """Return a string representation of a Band."""
        return f'{self.band_name} ({self.band_info})'

    def play(self):
        """print a string showing the musician playing their first (or no) instrument."""
        for band_list in self.band_lists:
            self.name = band_list.name
            self.instruments = band_list.instruments
            if not self.instruments:
                print(f"{self.name} needs an instrument!")
            else:
                print(f"{self.name} is playing: {self.instruments[0]}")
        return ''
