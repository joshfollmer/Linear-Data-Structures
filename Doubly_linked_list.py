#Josh Follmer
#Doubly linked list assignment

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Doubly_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_left(self, item):
        '''Inserts item at the beggining of the list, making it the head'''
        new_node = Node(item)
        #the heads previous pointer is the new node
        self.head.prev = new_node
        #the new nodes next pointer is the head
        new_node.next = self.head
        #designates the new node as the head
        self.head = new_node

    def append_right(self, item):
        '''Inserts item at the end of the list'''
        new_node = Node(item)
        #traverses the list, until last is set to the last item in the list, which will be set to the new node
        last = self.head
        while(last.next):
            last = last.next
        #the last item is now the new node
        last.next = new_node
        #the new nodes previous pointer goes  to whatever was last
        new_node.prev = last

    def pop_left(self):
        '''Deletes the head, the second item becomes the new head'''
        #saves the current head as a temp variable
        old_head = self.head
        #the new head is set to the second item
        self.head = old_head.next
        #clears the old head from the memory
        old_head = None
        #erases the new heads previous pointer
        self.head.prev = None


    def pop_right(self):
        '''Deletes the last item'''
        #traverses until the second to last item is selected
        second_last = self.head
        while(second_last.next.next):
            second_last = second_last.next
        #the item after the second to last is erased
        second_last.next = None
    
    def print_list(self):
        '''Prints the list'''
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def contains(self, key):
        '''Checks if an item exists in the list'''
        temp = self.head
        while(temp):
            if temp.data == key:
                return True
            temp = temp.next
        return False


