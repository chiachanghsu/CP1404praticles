from prac_09.musician import Musician


class Band(Musician):

    def __init__(self, band_name):
        super().__init__()
        self.band_info = []
        self.band_name = band_name
        self.band_info = ''

    def add(self, band_team):
        self.name = band_team.name
        self.instruments = band_team.instruments
        if self.band_info == '':
            self.band_info = Musician.__str__(band_team)
        else:
            self.band_info += ', ' + Musician.__str__(band_team)
        print(self.band_info)

    def __str__(self):
        return f'{self.band_name} ({self.band_info})'
