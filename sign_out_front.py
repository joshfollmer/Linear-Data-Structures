import circular_linked_list
from random import randint
from random import choice
import itertools
from datetime import datetime
from datetime import timedelta



class Sign:
    def __init__(self):
        self.slides = circular_linked_list.CircularLinkedList()
        #populates the list with slides
        for i in range(1, 21):
            self.slides.append_right(f"Slide {i}")


class Student:
    def __init__(self):
        arrive_times = [datetime(2021, 1, 1,8), datetime(2021, 1, 1,9,40), datetime(2021, 1, 1,11,10), datetime(2021, 1, 1,12,50), datetime(2021, 1, 1,14,30), datetime(2021, 1, 1,16,50), datetime(2021, 1, 1,17, 50), datetime(2021, 1, 1,19)]
        
        self.mw = choice(arrive_times)
        self.tt = choice(arrive_times)
        self.punc = randint(1, 10)

        self.name = choice("Lucas", "Will", "Noah", "Alex", "Josh", "Doug", "Mike", "John", "David", "Aaron", "Joye", "Abby", "Sofia", "Fiona", "Zoey", "Lily", "Hannah", "Bella", "Anna", "Elena", "Alice")


        
 
    def simulate(self, day):
        temp = sign.slides.head
        for i in range(randint(1, 21)):
            temp = temp.next
        
        

        if day == 1 or day == 3:
            arrive = self.mw 
        if day == 2 or day == 4:
            arrive = self.tt

        tardy = randint(1,2)
        if tardy == 1:
            arrive.minute -= self.punc
            self.speed = randint(20, 30)
        if tardy == 2:
            arrive.minute += self.punc
            self.speed = randint(30, 40)

            

        t = datetime(2021, 1, 1, 7,50)
        while t.hour < 20:
            temp = temp.next
            if t.time == arrive
            t.second += 20

        # seen_slides = []
        # seen_slides.append(temp.data)
        # for i in range(4):
        #     temp = temp.next
        #     seen_slides.append(temp.data)
        # return seen_slides

    def see_slides(self):


    # def store_slides(self):
    #     total_slides = []
    #     for i in range(4):
    #         total_slides.append(s.simulate())
    #     total_slides = list(itertools.chain.from_iterable(total_slides))
        
    #     total_slides = set(total_slides)
    #     dec = len(total_slides) / 20
    #     percent = '{:.0%}'.format(dec)
    #     print(percent)
        


sign = Sign()
s = Student()
s.store_slides()