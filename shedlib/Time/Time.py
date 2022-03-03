class Time:
    __slots__ = ('__seconds')

    def __init__(self, seconds):
        self.__seconds = seconds

    @property
    def splited(self):
        ''' Returns a list in format [hours, minutes, seconds] '''
        return [self.__seconds//3600, self.__seconds//60%60, self.__seconds%60]

    def __sub__(self, other):
        return Time(abs( self.__seconds - other.__seconds ))

    def __eq__(self, other):
        return self.__seconds == other.__seconds

    def __gt__(self, other):
        return self.__seconds > other.__seconds

    def __ge__(self, other):
        return self > other or self == other

    def __lt__(self, other):
        return self.__seconds < other.__seconds

    def __le__(self, other):
        return self < other or self == other

    def __ne__(self, other):
        return not self == other
