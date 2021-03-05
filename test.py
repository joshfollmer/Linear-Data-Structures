
from datetime import datetime
from datetime import timedelta

#t = time(7,50)
#print(t)
# for i in range(100):
#     t += datetime.timedelta(seconds = 3)
#     print(t.time())
 
#t = time(8, 10, 20)
t = datetime(2021, 1, 1, 23, 59, 59)
print(t.time())
x = t + timedelta(seconds = 3)
print(x.time())