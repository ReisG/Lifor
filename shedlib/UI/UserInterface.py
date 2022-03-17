

class UserInterface:
   """Basic user interface class"""
   def __init__(self) -> None:
      """Initialization method"""
      self.queue = []

   def update(self):
      """Main method. Update current scene"""
      pass

   def append_points(self, *points) -> None:
      """Append points in queue to show. Takes format [<name>, <is started>, <time left>]"""
      for point in points:
         self.queue.append(point)
