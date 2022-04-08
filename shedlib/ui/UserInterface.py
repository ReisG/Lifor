from shedlib.time.Time import Time

class UserInterface:
   """Basic user interface class"""
   def __init__(self) -> None:
      """Initialization method"""

      self.queue = []
      """queue to show"""

   def update(self):
      """Main method. Update current scene"""
      pass
    
   def append_points(self, name: str = "event", started: bool = True, time: Time = Time(seconds=0)) -> None:
      """
      Append points in queue to show.

      Parameters:
         name (str): The name of event
         started (bool): The flag that show if event if going on now or not
         time (Time): The time to start/end of event
      """

      self.queue.append([name, started, time])