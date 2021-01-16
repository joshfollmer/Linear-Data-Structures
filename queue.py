#Josh Follmer
#Queue data structure

class Queue:
    def __init__(self, list):
        self.list = list

    def append(self, new_item):
        self.list.insert(0, new_item)
        return self.list

    def pop(self):
        del self.list[-1]
        return self.list

    def contains(self, check_item):
        for i in self.list:
            if i == check_item:
                return True
        return False

