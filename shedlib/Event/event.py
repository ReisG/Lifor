from shedlib.Time.Time import Time
import csv


class Event:
    def __init__(self, id: int, name: str, start: Time, end: Time, day: str):
        """Class for event"""
        # self.__data = [ident, name, start, end, day]
        self.__id = id
        self.__name = name
        self.__start = start
        self.__end = end
        self.__day = day

    # def __repr__(self):
    #    return f"Event({self.__data})"
