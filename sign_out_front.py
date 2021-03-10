import circular_linked_list
from random import randint
from random import choice
import itertools
from datetime import datetime, time
from datetime import timedelta
from math import ceil


class Sign:
    def __init__(self):
        self.slides = circular_linked_list.CircularLinkedList()
        #populates the list with slides
        for i in range(1, 21):
            self.slides.append_right(f"Slide {i}")


class Student:
    def __init__(self):
        arrive_times = [datetime(2021, 1, 1,8), datetime(2021, 1, 1,9,40), datetime(2021, 1, 1,11,10), datetime(2021, 1, 1,12,50), datetime(2021, 1, 1,14,30), datetime(2021, 1, 1,16,50), datetime(2021, 1, 1,17, 50), datetime(2021, 1, 1,19)]
        names = ["Lucas", "Will", "Noah", "Alex", "Josh", "Doug", "Mike", "John", "David", "Aaron", "Joye", "Abby", "Sofia", "Fiona", "Zoey", "Lily", "Hannah", "Bella", "Anna", "Elena"]
        self.mw = choice(arrive_times)
        self.tt = choice(arrive_times)
        self.punc = randint(1, 10)
        self.seen_slides = []
        self.name = choice(names)
 
    def simulate(self, day):
        self.temp = sign.slides.head
        for i in range(randint(1, 21)):
            self.temp = self.temp.next
        
        

        if day == 1 or day == 3:
            arrive = self.mw 
        if day == 2 or day == 4:
            arrive = self.tt

        tardy = randint(1,2)
        if tardy == 1:
            arrive -= timedelta(minutes=self.punc)
            self.speed = randint(20, 30)
        if tardy == 2:
            arrive += timedelta(minutes=self.punc)
            self.speed = randint(30, 40)     

        t = datetime(2021, 1, 1, 7,50)

        for i in range(2046):
            self.temp = self.temp.next
            if t == arrive:
                self.see_slides()
            t += timedelta(seconds=20)

 

    def see_slides(self):
        #we need to find out how long they can see the sign for
        #first we find the feet per second, found by multiplying their current speed by 1.47
        fps = self.speed * 1.47
        #we divide the number of feet where they can see the sign and divide it by the feet per second, giving us the number of seconds they can see the sign for
        #i found 2205 by taking the mean amount of time of 60 seconds, assuming thats at the speed limit of 25 mph, finding the ft/s of 25 nad multiplying that by 60
        time_seeing = 2205 / fps
        #number of slides seen is the number of seconds divided by 20, rounded up. note that a decimal number refers to the amount of time seeing the slide, not the slide itself
        num_of_slides = ceil(time_seeing / 20)
        
        for i in range(num_of_slides):
            self.seen_slides.append(self.temp)
            self.temp = self.temp.next
        
        
def start_program():
    #try:
    start = input("Start simulation? Y/N\n")
    if start == 'Y' or start == 'y' or start == 'yes' or start == 'Yes':
        s = Student()
        for i in range(1, 5):
            s.simulate(i)
        s.seen_slides = set(s.seen_slides)
        print(f"{s.name} saw {len(s.seen_slides)} slides")
    elif start == 'N' or start == 'n' or start == 'no' or start == 'No':
        return          
    # except:
    #     print("Please input valid command")
    #     start_program()

sign = Sign()
start_program()