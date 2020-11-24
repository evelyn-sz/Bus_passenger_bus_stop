class Bus:
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passengers = []
       
    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.passengers)

    def pick_up(self, person):
        self.passengers.append(person)

    def drop_off(self, person):
        self.passengers.remove(person)

    def empty(self):
        self.passengers = []
        # self.passengers.clear()
        # OR
        # for passenger in self.passengers:
        #   self.passengers.pop()
        # because it's more polite
        # REASON: while looking at 1, removes 4
        #  while looking at 2, removes 3
        # and stops. so still 2 passengers left
        # .remove will also cause issues:
        # each time a loop is run, lest of elements shift to the left


    # that's wrong
    # def pick_up_from_stop(self, bus_stop):
    #     for person in bus_stop.queue:
    #         if person.destination == self.destination:
    #             self.passengers.extend(bus_stop.person)
    #             bus_stop.clear(person)

    def pick_up_from_stop(self, bus_stop):
        for passenger in bus_stop.queue:
            if passenger.destination == self.destination:
                self.pick_up(passenger)
                bus_stop.remove_from_queue(passenger)
        for passenger in self.passengers:
            bus_stop.remove_from_queue(passenger)
