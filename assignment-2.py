import math 
from typing import List

# -----------------Write a function that prints your name 5 times.
def print_name(name:str) -> None:
    for i in range(1,6):
        print(f"{i}. My name is {name}")

# ----------------- Write a function that takes 2 numbers and prints their sum.
def print_sum(a:int, b:int)-> str:
    return f"Sum is {a+b}"

# ----------------- Write a function that returns the cube of a number.
def print_cube(num:int) -> str:
    return f"Cube is {num**3}"

# ----------------- Write a function that checks if a number is even or odd.
def check_num(num:int) -> str:
    if(num%2 == 0): return f"Number {num} is even"
    else : return f"Number {num} is odd"

# Write a function that asks the user for age and prints if adult or not.
def check_age(age:int) -> str:
    if(age >=30): return 'Person is adult'
    else: return 'Person is not adult'

# Write a function that reverses a string.
def reverse_string(string:str)-> str:
    return string[::-1]

# Write a function that takes marks of 3 subjects and returns average.
def average(marks_1:int, marks_2:int, marks_3:int) -> str:
    average = (marks_1 + marks_2 + marks_3) / 3
    return f"Average is {average}"

# Write a function that takes a sentence and returns number of words.
def return_length(sentence:str) -> str:
    return f"{len(sentence.split(" "))} words"

# Write a function that takes a number and checks if it is prime.
def check_prime(num:int) -> str:
    if num > 1:
        for i in range(2,int(math.sqrt(num)) + 1):
            if( num % i == 0):
                return f"Number {num} is not prime"
        return f"Number {num} is prime"
    else :
        return "Please ensure number must be greater than 0"

# Write a function that calculates factorial of a number.
def calculate_factorial(num:int) -> str:
    factorial = 1
    for i in range(1,num+1):
        factorial *= i
    return f"Factorial is {factorial}"

# Write a function that takes a string and returns its length.
def string_length(string:str) -> str:
    return f'Length of string : {len(string)}'

# Write a function that prints multiplication table of a number.
def table(num:int) -> str:
    for i in range(1,11):
        print(f"{num} {i} is to {num*i}")

# Write a function that takes a list and returns the maximum value.
def max_value(lst:List[int]) -> str:
    return f"Maximum value : {max(lst)}"