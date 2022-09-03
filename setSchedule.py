from shedlib.Time.Time import Time
from os import system

WEEK_DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

datadir = '.data'

for i in range(7):
   system("cls||clear")
   print(f"{WEEK_DAYS[i]}")
   inp = input("Enter \"/make\" to create schedule of this day or \"/next\" to go to following day >>> ")

   if inp == "/make":
      with open(f"{datadir}/{WEEK_DAYS[i][0:3]}.shdl", "w") as day:
         print("To finish schedule enter \"/next\"")

         inp = input("Enter name of event or command >>> ")
         event = ""    
         while inp != "/next":
            event = inp + "$#$"

            inp = input("Enter start time in format hh:mm:ss >>> ")
            start = Time()
            start.set_in_hms_format(*list(map(int, inp.replace(" ", "").split(":"))))
            event += str(start.get_seconds()) + "$#$"

            inp = input("Enter end time in format hh:mm:ss >>> ")
            end = Time()
            end.set_in_hms_format(*list(map(int, inp.replace(" ", "").split(":"))))
            event += str(end.get_seconds())

            print(event, file=day)

            inp = input("Enter name of event or command >>> ")