from shedlib.UI.UserInterface import UserInterface
from shedlib.Time.Time import Time
from os import system


class ConsoleInterface(UserInterface):
    """
    Console user interface class

    Class fields:
        created_object: the only class object

    Object fields:
        __queue (tuple): event queue list

    Methods:
        update(): update current scene
        show_msg(msg="Hello, World!): write message in console
        show_event(name="Event", started=True, time=Time(seconds=0)): write info about event in console
        get_log(): get user input from console
        __queue_sort(): sort queue
    """

    created_object = None

    def __init__(self) -> None:
        """Initialization method"""
        super().__init__()

    def __new__(cls, *args, **kwargs):
        if cls.created_object is None:
            cls.created_object = super().__new__(cls)
            cls.created_object.__init__(args, kwargs)
        return cls.created_object

    def update(self) -> None:
        super().update()
        # clear console
        self.clear()
        
        # sort queue
        self.__queue_sort()

        # outputting cycle
        for point in self.queue:
            self.show_event(name=point[0], started=point[1], time=point[2])

        # clear queue
        self.queue.clear()

    def show_event(self, name: str = "Event", started: bool = True, time: Time = Time(seconds=0)) -> None:
        """
        Write info about event in console

        Parameters:
            name (str): The name of event
            started (bool): The flag that show if event if going on now or not
            time (Time): The time to start/end of event
        """

        # form log
        log = f"{name}: {time}"

        # add event status to log
        if started:
            log = f"# {log} left"
        else:
            log = f"{log} to beginning"

        # output log
        self.show_msg(msg=log)

    def __queue_sort(self):
        """Method to sort queue"""
        go = []
        """list for current events"""
        wait = []
        """list for next events"""

        # split queue to "go" and "wait"
        for point in self.queue:
            if point[1]:
                go.append(point)
            else:
                wait.append(point)

        # sort lists
        go.sort(key= lambda a: a[2])
        wait.sort(key= lambda a: a[2])

        # form final queue
        self.queue = go + wait

    @staticmethod
    def show_msg(msg: str = "Hello, World!") -> None:
        """
        Write message in console

        Parameters:
            msg (str): The message to show
        """
        print(msg)

    @staticmethod
    def get_log() -> str:
        """
        Get user input from console

        Returns:
            (str): The log that user input in console
        """
        return input(">>>")

    @staticmethod
    def clear():
        """
        Clear console
        """
        system("cls||clear")