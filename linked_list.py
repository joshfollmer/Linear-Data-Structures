#Josh Follmer
#linked lsit assignment

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
        '''puts a new item at the start of the list, making it the new head'''
        #makes a new node
        new_node = Node(item)
        #the new node is set to the head
        new_node.next = self.head
        #the head is now this new node
        self.head = new_node
        
    def append_right(self, item):
        new_node = Node(item)
        #starts at the head
        last = self.head
        #traverses the list. each time a next node exists, move on to the next and set the variable to it
        while(last.next):
            last=last.next
        #once it reaches the last node, set the next node to the new one
        last.next = new_node
        

    def pop_left(self):
        #saves the current head as a temp variable
        old_head = self.head
        #the second node now becomes the head
        old_head.next.data = self.head
        #deletes the old head
        old_head = None

    #this is based from https://www.geeksforgeeks.org/remove-last-node-of-the-linked-list/#:~:text=Approach%3A%20To%20delete%20the%20last,pointer%20of%20that%20node%20null.&text=Create%20an%20extra%20space%20secondLast,till%20the%20second%20last%20node.&text=delete%20the%20last%20node%2C%20i.e.,second%20last%20node%20delete(secondLast.
    def pop_right(self):
        second_last = self.head
        while(second_last.next.next):
            second_last = second_last.next
        second_last.next = None
           
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
        
    def get_len(self):
        temp = self.head
        length = 0
        while(temp):
            length += 1
            temp = temp.next
        return length

 

#this  is justan example of how this works. this will create a list of 1, 2, 3
#first initialize the list
l = LinkedList()
#the head is getting assigned with 1
l.head = Node(1)


l.append_right(2)
l.append_right(3)

l.pop_left()

l.print_list()