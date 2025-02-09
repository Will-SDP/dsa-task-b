import heapq 
from plane import Plane

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
