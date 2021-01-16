#Josh Follmer 
#Stack structure assignment


class Stack:
    def __init__(self, list):
        #iniatilsez self.list as the list that was passed to it
        self.list = list


    def append(self, new_item):
        #puts the passed item into the first spot
        self.list.insert(0, new_item)
        return self.list

    def pop(self):
        #deletes the first item in the list
        del self.list[0]
        return self.list

    def contains(self, check_item):
        #loops through, if i is equal to the given item it will return true
        for i in self.list:
            if i == check_item:
                return True
        #if the method is still running the item is not in the list, so it returns false
        return False
