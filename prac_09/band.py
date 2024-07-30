from prac_09.musician import Musician


class Band(Musician):

    def __init__(self, band_name):
        super().__init__()
        self.band_name = band_name
        self.band_lists = []

    def add(self, band_team):
        self.name = band_team.name
        self.instruments = band_team.instruments
        self.band_lists.append(band_team)

    def __str__(self):
        return f'{self.band_name} ({self.band_lists})'
