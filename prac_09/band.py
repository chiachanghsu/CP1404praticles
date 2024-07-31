from prac_09.musician import Musician


class Band(Musician):

    def __init__(self, band_name):
        super().__init__()
        self.band_name = band_name
        self.band_info = ''
        self.band_lists = []

    def add(self, band_team):
        self.name = band_team.name
        self.band_lists.append(band_team)
        if self.band_info == '':
            self.band_info = Musician.__str__(band_team)
        else:
            self.band_info += ', ' + Musician.__str__(band_team)

    def __str__(self):
        return f'{self.band_name} ({self.band_info})'

    def play(self):
        for band_list in self.band_lists:
            self.name = band_list.name
            self.instruments = band_list.instruments
            if not self.instruments:
                print(f"{self.name} needs an instrument!")
            else:
                print(f"{self.name} is playing: {self.instruments[0]}")
        return ''
