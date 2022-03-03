from shedlib.UI.UserInterface import UserInterface


class ConsoleInterface(UserInterface):
   """Console user interface class"""
   def __init__(self) -> None:
      """Initialization method"""
      super().__init__()

   def update(self) -> None:

      super().update()

   def show_msg(self, msg: str = "Hello, World!") -> None:
      """Write message in console"""
      print(msg)

   def get_log(self) -> str:
      """Get users input from console"""
      return input(">>>")