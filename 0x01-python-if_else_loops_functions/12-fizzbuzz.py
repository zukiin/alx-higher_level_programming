#!/usr/bin/python3

def fizzbuzz():
    n = 1
    str_1 = "Fizz"
    str_2 = "Buzz"
    str_3 = "FizzBuzz"

    while(n < 101):
        if (n % 3 == 0):
            print("{}".format(str_1), end=" ")
        elif (n % 5 == 0):
            print("{}".format(str_2), end=" ")
        elif (n % 3 == 0 and n % 5 == 0):
            print("{}".format(str_3), end=" ")
        else:
            print("{}".format(n), end=" ")

        n += 1
