#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
status = ""
last_digit = str(number)
last_digit = last_digit[len(last_digit) - 1]
if number < 0:
    last_digit = int(last_digit) * -1
if (int(last_digit) < 6) and (int(last_digit) != 0):
    status = "and is less than 6 and not 0"
elif (int(last_digit) > 5):
    status = "and is greater than 5"
else:
    status = "and is 0"
print("Last digit of", number, "is", last_digit, status)
