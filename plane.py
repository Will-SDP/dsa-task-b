class Plane:
    def __init__(self, label, fuel, distance):
        self.__label = label
        self.__fuel = fuel
        self.__distance = distance
        self.__priority = None
        self.calculate_priority(self.__fuel, self.__distance)
        self.__minimum_fuel = False

    def __lt__(self, obj):
        return self.__priority < obj.__priority    
    
    def __repr__(self):
        return f"Plane({self.__label}, Priority={self.__priority})"    

    def calculate_priority(self, fuel, distance):
        if self.__priority != 0:
            self.__priority = abs(fuel - distance) + (fuel + distance)
    
    def get_priority(self):
        return int(self.__priority)
    
    def get_label(self):
        return self.__label
    
    def set_minimum_fuel(self):
        self.__minimum_fuel = True
    
    def mayday(self):
        self.__priority = 0