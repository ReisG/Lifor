from shedlib.Time.Time import Time


class Event:
    def __init__(self, identificator: int, name: str, start: Time, end: Time):
        """Class for event"""
        self.data = [identificator, name, start, end]

    def get_data(self):
        return self.data
