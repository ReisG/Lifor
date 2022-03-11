from shedlib.UI.UserInterface import UserInterface


class ConsoleInterface(UserInterface):
    """Console user interface class"""

    def __init__(self) -> None:
        """Initialization method"""
        super().__init__()

    def update(self) -> None:
        super().update()

        for point in self.queue:
            self.show_point(name=point[0], last=point[1])

        self.queue.clear()

    def show_msg(self, msg: str = "Hello, World!") -> None:
        """Write message in console"""
        print(msg)

    def show_point(self, name: str = "Nothin\'", last: int = 0) -> None:
        """Write info about point in console"""
        log = f"{name} will last next {last} sec."
        self.show_msg(msg=log)

    def get_log(self) -> str:
        """Get users input from console"""
        return input(">>>")
