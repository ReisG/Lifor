from shedlib.Time.Time import Time
from shedlib.Event.event import Event

class Parser:
    __slots__ = ()

    datadir = '.data'
    filetype = 'shdl'

    def __init__(self):
        raise SyntaxError('You cannot create instance of this class. Use class methods')

    @classmethod
    def get(self, weekday=None):
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        if weekday in days:
            return self.__parse(f'{Parser.datadir}/{weekday}.{Parser.filetype}')
        else:
            raise ValueError(f'There is no day <{weekday}>')

    def __parse(filename=''):
        '''
            Method for parsing .shdl files
            returns list of events
        '''
        sep_symb = '$#$'

        result = []
        with open(filename, 'r') as file:
            id = 0
            event = file.readline()
            while (len(event) > 1 or id == 0):
                event = event.split(sep_symb)
                result.append(Event( id, event[0], Time(int(event[1])), Time(int(event[2])) ))
                id += 1
                event = file.readline()
        return result
