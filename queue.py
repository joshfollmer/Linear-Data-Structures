#Josh Follmer
#Queue data structure

class Queue:
    def __init__(self, list):
        self.list = list

    def append(self, new_item):
        #inserts the passed item into the first place
        self.list.insert(0, new_item)
        return self.list

    def pop(self):
        #saves the last item as a variable
        removed_item = self.list[-1]
        #removes the last item from the  list
        del self.list[removed_item]
        return self.list, removed_item

    def contains(self, check_item):
        #loops through, if the item to be checked is in the list, return true. otherwise return false
        for i in self.list:
            if i == check_item:
                return True
        return False

