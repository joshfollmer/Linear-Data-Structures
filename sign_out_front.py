import circular_linked_list
from random import randint
import itertools

class Student:
    def __init__(self):
        self.slides = circular_linked_list.CircularLinkedList()
        #populates the list with slides
        for i in range(1, 21):
            self.slides.append_right(f"Slide {i}")

    def simulate(self):
        temp = self.slides.head
        for i in range(randint(1, 21)):
            temp = temp.next

        seen_slides = []
        seen_slides.append(temp.data)
        for i in range(4):
            temp = temp.next
            seen_slides.append(temp.data)
        return seen_slides

    def store_slides(self):
        total_slides = []
        for i in range(4):
            total_slides.append(s.simulate())
        total_slides = list(itertools.chain.from_iterable(total_slides))
        
        total_slides = set(total_slides)
        dec = len(total_slides) / 20
        percent = '{:.0%}'.format(dec)
        print(percent)
        



s = Student()
s.store_slides()