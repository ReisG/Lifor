class Time:
    ''' Object for storing time '''

    __slots__ = ('__seconds',)

    def __init__(self, seconds:int=0):
        self.__seconds = seconds

    @property
    def splited(self):
        ''' Returns a list in format [hours, minutes, seconds] '''
        return [self.__seconds // 3600, self.__seconds // 60 % 60, self.__seconds % 60]

    def get_seconds(self):
        return self.__seconds

    def set_in_hms_format(self, hours:int, minutes:int, seconds:int):
        ''' This method will help you to write data in object in hours:minutes:seconds format

        Parameters:
            int hours, minutes, seconds: parts
        '''
        self.__seconds = hours*3600 + minutes*60 + seconds

    def __sub__(self, other):
        return Time(abs(self.__seconds - other.__seconds))

    def __eq__(self, other):
        return self.__seconds == other.__seconds

    def __gt__(self, other):
        return self.__seconds > other.__seconds

    def __ge__(self, other):
        return self > other or self == other

    def __lt__(self, other):
        return self.__seconds < other.__seconds

    def __le__(self, other:Time):
        return self < other or self == other

    def __ne__(self, other:Time):
        return not self == other

    def __str__(self) -> str:
        t = self.splited
        res = ""
        if t[0] > 0:
            res += f"{t[0]} h "
        if t[1] > 0:
            res += f"{t[1]} min "
        res += f"{t[2]} sec"

        return res
