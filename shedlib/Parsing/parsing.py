from shedlib.Time.Time import Time
from shedlib.Event.event import Event

class Parser:
    ''' Class helping getting day schedule (parsing .shdl files)'''
    __slots__ = ()

    __datadir = '.data'
    __filetype = 'shdl'

    __sep_symb = '$#$'

    def __init__(self):
        ''' This class cannot have instances. Don't use this method '''
        raise SyntaxError('You cannot create instance of this class. Use class methods')

    @staticmethod
    def get(weekday=None):
        ''' Returns sorted list of events on selected day
            Parameters:
                weekday (str): three fisrt letters of selected day (Mon, Tue, Wed, Thu, Fri, Sat, Sun)
        '''
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        if weekday in days:
            day_schedule = Parser.__parse(f'{Parser.__datadir}/{weekday}.{Parser.__filetype}')
            return Parser.__sort(day_schedule)
        else:
            raise ValueError(f'There is no day <{weekday}>')

    @staticmethod
    def __sort(day_schedule=[]):
        ''' Sorting events FIRST by starting time, and if it's equal, by ending time
            Parameters:
                day_schedule (list): list of days events
        '''
        day_schedule.sort()
        return day_schedule

    @staticmethod
    def __parse(filename=''):
        '''
            Method for parsing .shdl files
            returns list of events
            Parameters:
                filename (str): full (from running file) trace to parsing .shdl file
        '''
        result = []
        with open(filename, 'r') as file:
            id = 0
            event = file.readline()
            while (len(event) > 1 or id == 0):
                event = event.split(Parser.__sep_symb)
                result.append(Event( id, event[0], Time(int(event[1])), Time(int(event[2])) ))
                id += 1
                event = file.readline()
        return result
