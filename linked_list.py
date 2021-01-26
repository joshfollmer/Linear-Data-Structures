#Josh Follmer
#linked lsit assignment

#this is a class for the things that are getting stored in the list
class Node:
    def __inti__(self, data):
        #the variable for the content of the item
        self.data = data
        #this will be the connection to the next node. it is purposefully left undefined so it can be assinged later, but it needs to exist first
        self.next = None

#this is a class for the head node, or the one that will start the list
class LinkedList:
    def __init__(self):
       #this is for the data that will be stored in the head
       self.head = None 

#this  is justan example of how this works. this will create a list of 1, 2, 3
#first initialize the list
l = LinkedList()
#the head is getting assigned with 1
l.head = Node(1)
#the second item is assigned 2
second = Node(2)
#and 3
third = Node(3)
#these set up the pointers between them. the head points to the second, and the second points to the third
l.head.next = second
second.next = third