from shedlib.ui import ConsoleInterface
from shedlib.parsing import Parser
from shedlib.time import Time
import time


class LiforApp:
    """Main application class"""

    __slots__ = ('__schedule', '__cli', '__cur_time')

    def __init__(self):
        """Initialize object"""
        __WEEK_DAY = time.ctime().split()[0]  # must be private

        self.__schedule = Parser.get(__WEEK_DAY) # private
        self.__cli = ConsoleInterface() # private
        self.__cur_time = Time(0) # private

    def run(self) -> None:
        """Start a main program cycle"""
        program_end = False

        while not program_end:
            self.__update_time()

            self.__make_scene()

            self.__cli.update()
            time.sleep(1)

    def __update_time(self) -> None:
        """Update current time"""
        time_durty = time.strptime(time.ctime())
        self.__cur_time.set_in_hms_format(time_durty.tm_hour, time_durty.tm_min, time_durty.tm_sec)

    def __make_scene(self) -> None:
        """Parse activities and send them to interface"""
        for activity in self.__schedule:
            if (self.__cur_time <= activity.start):
                # activity hasn't started yet
                self.__cli.append_points(activity.name, False, (activity.start - self.__cur_time))
            elif (activity.start <= self.__cur_time <= activity.end):
                # activity is already running
                self.__cli.append_points(activity.name, True, (activity.end - self.__cur_time))
            # otherwise we don't send it to Interface

