class BusStop:
    def __init__(self, name):
        self.name = name
        self.queue = []
        
    def queue_length(self):
        return len(self.queue)

    def add_to_queue(self, person):
        self.queue.append(person)

    def remove_from_queue(self, person):
        self.queue.remove(person)

    def clear(self):
        self.queue = []
        # self.queue.clear()