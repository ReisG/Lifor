from shedlib.UI.UserInterface import UserInterface
import os


class ConsoleInterface(UserInterface):
   """Console user interface class"""
   def __init__(self) -> None:
      """Initialization method"""
      super().__init__()
      self.__com_palette = {
         "show_msg": lambda x="Hello": self.show_msg(msg= x)
      }

   def update(self, command: str):
      com = command.split(" ")[0]
      args = command.replace(com+" ", "")
      self.__com_palette[com](args)

      return super().update()

   def show_msg(self, msg):
      """Write message in console"""
      if len(msg) == 0:
         msg = "Hello"
      print(msg)