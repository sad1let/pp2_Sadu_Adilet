# Write a Python program with builtin function to multiply all the numbers in a list



from functools import reduce

def multiply_list_numbers(lst):
    return reduce(lambda x, y: x*y, lst)

# Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters

def count_upper_lower(string):
    upper_count = 0
    lower_count = 0
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count

# Write a Python program with builtin function that checks whether a passed string is palindrome or not
def is_palindrome(s):
    return s == ''.join(reversed(s))

# Write a Python program that invoke square root function after specific milliseconds. Sample Input: 25100 2123 Sample Output: Square root of 25100 after 2123 miliseconds is 158.42979517754858
import time
import math

def sqrt_after_milliseconds(n, milliseconds):
    time.sleep(milliseconds/1000)
    result = math.sqrt(n)
    print(f"Square root of {n} after {milliseconds} milliseconds is {result}")

# Write a Python program with builtin function that returns True if all elements of the tuple are true.

def all_true(t):
    return all(t)