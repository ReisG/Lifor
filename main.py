from shedlib.UI.ConsoleInterface import ConsoleInterface as ConsoleInterface
from shedlib.Parsing.parsing import Parser as Parser
from shedlib.Time.Time import Time as Time
import time


def main():
    """Main function"""

    # Initializing progsses
    WEEK_DAY = time.ctime().split()[0]
    schedule = Parser.get(WEEK_DAY)
    Interface = ConsoleInterface()

    programm_end = False
    cur_time = Time(0)
    while not programm_end:
        time_durty = time.strptime(time.ctime())
        cur_time.set_in_hms_format(time_durty.tm_hour, time_durty.tm_min, time_durty.tm_sec)

        for activity in schedule:
            if (cur_time <= activity.start):
                # activity hasn't started yet
                Interface.append_points([activity.name, False, (activity.start - cur_time).splited])
            elif (activity.start <= cur_time <= activity.end):
                Interface.append_points([activity.name, True, (activity.end - cur_time).splited])

        Interface.update()
        time.sleep(1)



if __name__ == "__main__":
    main()
    quit()
