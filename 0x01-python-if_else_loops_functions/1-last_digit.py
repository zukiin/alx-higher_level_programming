#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

the_str = "Last digit of"
num_as_str = str(number)
last_num = int(num_as_str[-1])

if number < 0:                                                                  
     last_num = -last_num 

if last_num > 5:
    print(f"{the_str} {number} is {last_num} and is greater than 5")
elif last_num == 0:
    print(f"{the_str} {number} is {last_num} and is 0")
elif last_num < 6 and last_num != 0:
     print(f"{the_str} {number} is {last_num} and is less than 6 and not 0")
