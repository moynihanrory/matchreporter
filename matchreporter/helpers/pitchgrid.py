from matchreporter.constants import UNKNOWN_PITCH_SECTOR
from matchreporter.helpers.stringhelper import parseInt


class Grid(object):
    def __init__(self):
        self.x = { '1': range(0, 31),
                   '2': range(31, 71),
                   '3': range(71, 100)}

        self.y = { 'A': range(0, 9),
                   'B': range(9, 35),
                   'C': range(35, 65),
                   'D': range(65, 91),
                   'E': range(91, 100)}



    def _getSector(self, x, y):

        for xName, xValue in self.x.items():

            if x in xValue:
                for yName, yValue in self.y.items():

                    if y in yValue:
                        return xName + yName



    def getPitchSector(self, coordinates):
        if coordinates is None:
            return UNKNOWN_PITCH_SECTOR

        xValue = parseInt(coordinates[0:coordinates.find(':')])

        yValue = parseInt(coordinates[(coordinates.find(':') + 1)::])

        pitchSector = self._getSector(xValue, yValue)

        return pitchSector
