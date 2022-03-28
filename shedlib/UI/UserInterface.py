from shedlib.Time.Time import Time

class UserInterface:
   """Basic user interface class"""
   def __init__(self) -> None:
      """Initialization method"""

      self.queue = []
      """queue to show"""

   def update(self):
      """Main method. Update current scene"""
      pass

   def append_points(self, *points) -> None:
      """
      Append points in queue to show.

      first item in list is name of event;
      second - flag that shows if event is going on now or not;
      third - time to start/end of event;

      Parameters:
         *points(tuple[str, bool, Time]): list of events
      """

      for point in points:
         self.queue.append(point)
