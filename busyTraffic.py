class Event:
    def __init__(self, type: str, marker: int, speed: int):
        self.type = type
        self.marker = marker
        self.speed = speed

def busyTraffic(cars: list[list[int]]) -> list[list[int]]:
    events: list[Event] = []
    for i in cars:
        events.append(Event("o", i[0], i[2]))
        events.append(Event("c", i[1], i[2]))
    
    events.sort(key = lambda x: x.marker)
    
    total = count = 0
    prevMarker = events[0].marker
    result = []
    for i in events:
        if i.marker != prevMarker:
            result.append([prevMarker, i.marker, total / count])
            prevMarker = i.marker
        
        if i.type == "o":
            count += 1
            total += i.speed
        else:
            count -= 1
            total -= i.speed

    return result

    
cars = [[15, 17, 30], [15, 20, 20], [5, 15, 30]]
print(*busyTraffic(cars))
    