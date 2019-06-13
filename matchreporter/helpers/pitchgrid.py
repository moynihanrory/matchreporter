from matchreporter.constants import UNKNOWN_PITCH_SECTOR
from matchreporter.helpers.stringhelper import parseInt


class Grid(object):
    def __init__(self):
        # self.x = { '1': range(0, 31),
        #            '2': range(31, 71),
        #            '3': range(71, 100)}
        #
        # self.y = { 'A': range(0, 9),
        #            'B': range(9, 35),
        #            'C': range(35, 65),
        #            'D': range(65, 91),
        #            'E': range(91, 100)}
        self.x = { 'C': range(0, 22),
                   'B': range(22, 78),
                   'A': range(78, 100)}

        self.y = { '6': range(0, 15),
                   '5': range(15, 32),
                   '4': range(32, 50),
                   '3': range(50, 68),
                   '2': range(68, 85),
                   '1': range(85, 100)}

        self.rx = { 'C': 'A',
                   'B': 'B',
                   'A': 'C'}

        self.ry = { '6': '1',
                   '5': '2',
                   '4': '3',
                   '3': '4',
                   '2': '5',
                   '1': '6'}


    def _getSector(self, x, y):

        for xName, xValue in self.x.items():

            if x in xValue:
                for yName, yValue in self.y.items():

                    if y in yValue:
                        return yName + xName


    def _getReflectedSector(self, x, y):

        for xName, rxValue in self.rx.items():

            if x.lower() == rxValue.lower():
                for yName, ryValue in self.ry.items():

                    if y.lower() == ryValue.lower():
                        return yName.lower() + xName.lower()


    def getPitchSector(self, coordinates):
        if coordinates is None:
            return UNKNOWN_PITCH_SECTOR

        xValue = parseInt(coordinates[0:coordinates.find(':')])

        yValue = parseInt(coordinates[(coordinates.find(':') + 1)::])

        pitchSector = self._getSector(xValue, yValue)

        return pitchSector


    def getReflectedPitchSector(self, coordinates):
        if coordinates is None:
            return UNKNOWN_PITCH_SECTOR

        xValue = coordinates[0]

        yValue = coordinates[1]

        pitchSector = self._getReflectedSector(yValue, xValue)

        return pitchSector
