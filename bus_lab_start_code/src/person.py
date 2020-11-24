class Person:
    def __init__(self, name, age, destination):
        self.name = name
        self.age = age
        self.destination = destination
    
    def travel_to(self, bus_stop):
        self.destination = bus_stop
