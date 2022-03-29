from shedlib.Time.Time import Time
from shedlib.Event.event import Event

class Parser:
    __slots__ = ()

    __datadir = '.data'
    __filetype = 'shdl'

    __sep_symb = '$#$'

    def __init__(self):
        raise SyntaxError('You cannot create instance of this class. Use class methods')

    @staticmethod
    def get(weekday=None):
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        if weekday in days:
            day_schedule = Parser.__parse(f'{Parser.__datadir}/{weekday}.{Parser.__filetype}')
            return Parser.__sort(day_schedule)
        else:
            raise ValueError(f'There is no day <{weekday}>')

    @staticmethod
    def __sort(day_schedule=[]):
        day_schedule.sort()
        return day_schedule

    @staticmethod
    def __parse(filename=''):
        '''
            Method for parsing .shdl files
            returns list of events
        '''

        result = []
        with open(filename, 'r') as file:
            id = 0
            event = file.readline()
            while (len(event) > 1 or id == 0):
                event = event.split(Parser.sep_symb)
                result.append(Event( id, event[0], Time(int(event[1])), Time(int(event[2])) ))
                id += 1
                event = file.readline()
        return result
