import time
import math

def calculate_sqrt(number, milliseconds):
    time.sleep(milliseconds/1000)  
    return math.sqrt(number)

number = int(input("Enter a number: "))
milliseconds = int(input("Enter the number of milliseconds: "))

result = calculate_sqrt(number, milliseconds)
print(f"Square root of {number} after {milliseconds} milliseconds is {result}")