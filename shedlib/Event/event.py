from shedlib.Time.Time import Time

class Event:
    __slots__ = ('__data', '__name', '__start', '__end',)

    def __init__(self, id: int, name: str, start: Time, end: Time):
        """Class for event"""
        self.__id = id
        self.__name = name
        self.__start = start
        self.__end = end

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def start(self):
        return self.__start

    @property
    def end(self):
        return self.__end
