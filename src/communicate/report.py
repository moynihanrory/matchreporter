from abc import abstractmethod

class Report(object):
    def __init__(self, source):
        self.source = source

    @abstractmethod
    def generate(self, data):
        return NotImplemented