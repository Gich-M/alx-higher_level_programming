#!/usr/bin/python3
import random
number = random.randint(-10, 10)
for n in range(-10, 10):
    if n > 0:
        print(f"{n} is positive")
    elif n == 0:
        print(f"{n} is zero")
    else:
        print(f"{n} is negative")
