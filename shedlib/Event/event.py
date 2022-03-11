from Time.Time import Time


class Event:
    def __init__(self):
        self.data = []

    def initialize(self, identificator: int, name: str, start: Time, end: Time):
        self.data = [identificator, name, start, end]

