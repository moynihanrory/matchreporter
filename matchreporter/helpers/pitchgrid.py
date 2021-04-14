from matchreporter.constants import UNKNOWN_PITCH_SECTOR
from matchreporter.helpers.stringhelper import parse_int


class Grid:
    def __init__(self):

        self.x = { 'C': range(0, 22),
                   'B': range(22, 78),
                   'A': range(78, 100)}

        self.y = { '6': range(0, 15),
                   '5': range(15, 32),
                   '4': range(32, 50),
                   '3': range(50, 68),
                   '2': range(68, 85),
                   '1': range(85, 100)}

        self.rx = {'C': 'A', 'B': 'B', 'A': 'C'}
        self.ry = {'6': '1', '5': '2', '4': '3', '3': '4', '2': '5', '1': '6'}


    def _get_sector(self, x, y):

        for x_name, x_value in self.x.items():

            if x in x_value:
                for y_name, y_value in self.y.items():

                    if y in y_value:
                        return y_name + x_name


    def _get_reflected_sector(self, x, y):

        for x_name, rx_value in self.rx.items():

            if x.lower() == rx_value.lower():
                for y_name, ry_value in self.ry.items():

                    if y.lower() == ry_value.lower():
                        return y_name.lower() + x_name.lower()


    def get_pitch_sector(self, coordinates):
        if coordinates is None:
            return UNKNOWN_PITCH_SECTOR

        x_value = parse_int(coordinates[0:coordinates.find(':')])

        y_value = parse_int(coordinates[(coordinates.find(':') + 1)::])

        pitchSector = self._get_sector(x_value, y_value)

        return pitchSector


    def get_reflected_pitch_sector(self, coordinates):
        if coordinates is None:
            return UNKNOWN_PITCH_SECTOR

        x_value = coordinates[0]

        y_value = coordinates[1]

        pitch_sector = self._get_reflected_sector(y_value, x_value)

        return pitch_sector
