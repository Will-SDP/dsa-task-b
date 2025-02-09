import heapq 

class Plane:
    def __init__(self, label, fuel, distance):
        self.__label = label
        self.__fuel = fuel
        self.__distance = distance
        self.__priority = None
        self.calculate_priority(self.__fuel, self.__distance)

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
    
    def mayday(self):
        self.__priority = 0


planes = [    
    {'id': 'PlaneA', 'distance': 50, 'fuel': 20},
    {'id': 'PlaneB','distance': 30, 'fuel': 60},
    {'id': 'PlaneC','distance': 70, 'fuel': 30},
    {'id': 'PlaneD','distance': 10, 'fuel': 90},
    {'id': 'PlaneE','distance': 100, 'fuel': 10}
    

]

new_plane = {'id': 'PlaneF','distance': 5, 'fuel': 30}

priority_queue = [] 

for p in planes:
    heapq.heappush(priority_queue, Plane(p['id'], p['fuel'], p['distance']))
    

## We expect plane A to be next to land
print(heapq.heappop(priority_queue))

## Add plane F which is very close to the runway 
heapq.heappush(priority_queue, Plane(new_plane['id'], new_plane['fuel'], new_plane['distance']))

## This should be the next plane out of the queue 
print(heapq.heappop(priority_queue))

## Plane B should be the next plane to come of the queue
print(heapq.heappop(priority_queue))
