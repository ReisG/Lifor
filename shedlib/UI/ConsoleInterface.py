from shedlib.UI.UserInterface import UserInterface


class ConsoleInterface(UserInterface):
    """Console user interface class"""

    def __init__(self) -> None:
        """Initialization method"""
        super().__init__()

    def update(self) -> None:
        super().update()

        self.__queue_sort()

        for point in self.queue:
            self.show_point(name=point[0], last=point[2], started=point[1])

        self.queue.clear()

    def show_msg(self, msg: str = "Hello, World!") -> None:
        """Write message in console"""
        print(msg)

    def show_point(self, name: str = "Nothin\'", last: int = 0, started: bool = True) -> None:
        """Write info about point in console"""
        log = f"{name}: {last}"

        if started:
            log = f"# {log} left"
        else:
            log = f"{log} to beginning"

        self.show_msg(msg=log)

    def get_log(self) -> str:
        """Get users input from console"""
        return input(">>>")

    def __queue_sort(self):
        """Method to sort queue"""
        go = []
        wait = []

        for point in self.queue:
            if point[1]:
                go.append(point)
            else:
                wait.append(point)

        go.sort(key= lambda a: a[2])
        wait.sort(key= lambda a: a[2])

        self.queue = go + wait
