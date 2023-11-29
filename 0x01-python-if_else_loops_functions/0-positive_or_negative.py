#!/usr/bin/python3
import random

# Assign a random signed number to the variable number
number = random.randint(-10, 10)

# Print the number
print(f'The number is: {number}')

# Check if the number is positive, negative, or zero
if number > 0:
    print('The number is positive')
elif number == 0:
    print('The number is zero')
else:
    print('The number is negative')
