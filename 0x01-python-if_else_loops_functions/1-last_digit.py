#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

temp = number

if number < 0:
    number = -(number)

lastDigit = number % 10
if temp < 0:
    number = temp
    lastDigit = (lastDigit)

if lastDigit > 5:
    output = "and is greater than 5"
elif lastDigit == 0:
    output = "and is 0"
elif lastDigit < 6:
    output = "and is less than 6 and not 0"

print("Last digit of {:d} is {:d}".format(number, lastDigit), output)
