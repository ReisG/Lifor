from shedlib.Time.Time import Time
import csv


class Event:
    def __init__(self, ident: int, name: str, start: Time, end: Time, day: str):
        """Class for event"""
        self.__data = [ident, name, start, end, day]

    def __str__(self):
        return f"""
        ident: {self.__data[0]}, 
        name: {self.__data[1]}, 
        start: {self.__data[2].splited}, 
        end: {self.__data[3].splited}, 
        day: {self.__data[4]}"""

    def __repr__(self):
        return f"Event({self.__data})"

    def get_data(self):
        """Return data in format [id, name, start, end]"""
        return self.__data

    def set_data(self, ident=None, name=None, start=None, end=None, day=None) -> bool:
        """Set some data returns True if data has been set"""
        new_data = [ident, name, start, end, day]
        flag = False
        for i in range(len(new_data)):
            if new_data[i] is not None:
                self.__data[i] = new_data[i]
                flag = True
        return flag

    def save(self, filename="C:/Users/АДМИН/Desktop/Lifor/.data/data.csv"):
        """Save data to csv file returns True if data has been saved"""
        try:
            with open(filename, encoding="utf-8") as csvfile:
                csvreader = csv.reader(csvfile, delimiter=";", quotechar="\"")
                data = list(csvreader)

                add_data = self.__data.copy()
                add_data[2] = add_data[2].get_seconds()
                add_data[3] = add_data[3].get_seconds()

                data.append(add_data)

            with open(filename, "w") as csvfile:
                csvwriter = csv.writer(csvfile, delimiter=";", quotechar="\"", quoting=csv.QUOTE_NONNUMERIC)
                csvwriter.writerows(data)

            return True

        except FileNotFoundError:
            return False
