#!/usr/bin/python3
import random

number = random.randint(-10, 10)

# Check the value of 'number' and print whether it's positive, negative, or zero
if number > 0:
    print(f"The number {number} is positive")
elif number == 0:
    print("The number is zero")
else:
    print(f"The number {number} is negative")

