
#this is a class for the things that are getting stored in the list
class Node:
    def __init__(self, data):
        #the variable for the content of the item
        self.data = data
        #this will be the connection to the next node. it is purposefully left undefined so it can be assinged later, but it needs to exist first
        self.next = None

    

#this is a class for the head node, or the one that will start the list
class LinkedList:
    def __init__(self):
       #this is for the data that will be stored in the head
       self.head = None 

    def append_left(self, item):
        '''Puts a new item at the start of the list, making it the new head'''
        #makes a new node
        new_node = Node(item)
        #the new node is set to the head
        new_node.next = self.head
        #the head is now this new node
        self.head = new_node
        
    def append_right(self, item):
        '''Adds an item to the end'''
        new_node = Node(item)
        #starts at the head
        last = self.head
        if self.head is None:
            self.head = new_node
            return
        #traverses the list. each time a next node exists, move on to the next and set the variable to it
        while(last.next):
            last=last.next
        #once it reaches the last node, set the next node to the new one
        last.next = new_node
        

    def pop_left(self):
        '''Deletes the head, the second in the list becomes the new head'''
        #saves the current head as a temp variable
        old_head = self.head
        #the second node now becomes the head
        self.head = old_head.next
        #deletes the old head
        old_head = None


    #this is based from https://www.geeksforgeeks.org/remove-last-node-of-the-linked-list/#:~:text=Approach%3A%20To%20delete%20the%20last,pointer%20of%20that%20node%20null.&text=Create%20an%20extra%20space%20secondLast,till%20the%20second%20last%20node.&text=delete%20the%20last%20node%2C%20i.e.,second%20last%20node%20delete(secondLast.
    def pop_right(self):
        #this one is pretty redunant but i should be in the habit of making these
        '''deletes the last element in the list '''
        #makes a variable that will end up as the second last in the list
        second_last = self.head
        #while a node has two nodes in front of it, loops though the list
        while(second_last.next.next):
            second_last = second_last.next
        #removes the connection from the second last to the last
        second_last.next = None
        
           
    def print_list(self):
        '''Prints the list'''
        #sets a temp variable
        temp = self.head
        #while the current node exists
        while(temp):
            #prints the data
            print(temp.data)
            #changes to the next node
            temp = temp.next
        
    def get_len(self):
        '''Returns the lenth of the list'''
        #same thing as print_list, but adds one to the length each loop and returns the result
        temp = self.head
        length = 0
        while(temp):
            length += 1
            temp = temp.next
        return length

    def contains(self, key):
        '''Checks if the list contains the passed item'''
        temp = self.head
        while(temp):
            if temp.data == key:
                return True
            temp = temp.next
        return False

    def reverse(self):
        '''Reverses the order of the list'''
        #this works by reversing the pointers, so each node points to the item before it
        prev = None
        #function starts at the head
        current = self.head
        #while the selected node is not null
        while(current):
            #selects the next node 
            next = current.next
            #changes the pointer from the next node to the previous node
            current.next = prev
            #the next two lines select the next node for the next loop
            prev = current
            current = next
        #makes the formerly last item the new head
        self.head = prev
            
l = LinkedList()

l.reverse()
#l.print_list()      
 