#SECTION 2 - FUNCTIONS (20PTS TOTAL)

import math
import random

#PROBLEM 1 (Length of String - 3pts)
# Make a function which asks the user to enter a string, then prints the length of that string.
# You will need to use the input() function.
# Make a call to that function

def function():
    user_input = input("write something: ")
    length = len(user_input)
    print(length)
function()

import math
# PROBLEM 2 (Pythagorean theorem - 4pts)
# The Pythagorean theorem states that of a right triangle, the square of the
# length of the diagonal side is equal to the sum of the squares of the lengths
# of the other two sides (or a^2 + b^2 = c^2).
# Write a program that asks the user for the lengths of the two sides that meet at a right angle.
# Then calculate the length of the third side, and display it in a nicely formatted way.
# You may ignore the fact that the user can enter negative or zero lengths for the sides.

def pythag(a,b):
    c_squared = a**2 + b**2
    c = math.sqrt(c_squared)

    print("the length of the hypotenuse is", c)
a = int(input("enter a value for the side of a right triangle: "))
b = int(input("enter another value for the side of the right triangle: "))
pythag(a,b)

# PROBLEM 3 (Biggest, smallest, average - 4pts)
# Make a function to ask the user to enter three numbers.
# Then print the largest, the smallest, and their average, rounded to 2 decimals.
# Display the answers in a "nicely" formatted way.
# Make a call to your function.

def numbers(a,b,c):
    if a >= b and a >= c:
        print(a, "is the largest number you entered")
    if b > a and b >= c:
        print(b, "is the largest number you entered")
    if c > a and c > b:
        print(c, "is the largest number you entered")
    if a <= b and a <= c:
        print(a, "is the smallest number you entered")
    if b < a and b <= c:
        print(b, "is the smallest number you entered")
    if c < a and c < b:
        print(c, "is the smallest number you entered")
    average = (float(a + b + c) / 3)
    print("the average of the numbers is", float(round(average,2)))

a = int(input("enter a number: "))
b = int(input("enter another number: "))
c = int(input("enter one more number: "))
numbers(a,b,c)

# PROBLEM 4 (e to the... - 3pts)
# Calculate the value of e (from the math library) to the power of -1, 0, 1, 2, and 3.
# display the results, with 5 decimals, in a nicely formatted manner.


def e():
    print(round(math.e ** -1, 5))
    print(round(math.e ** 0, 5))
    print(round(math.e ** 1, 5))
    print(round(math.e ** 2, 5))
    print(round(math.e ** 3, 5))
e()

# Lee - Use a for loop for this (-0.5).  DRY principle.

# PROBLEM 5 (Random int - 3pts)
# Generate a random integer between 1 and 10 (1 and 10 both included),
# but only use the random() function (randrange is not allowed here)

random_int = int(random.random() * 10)
print("the random number from 1 to 10 is", random_int)

## Lee - This problem set is based on functions.  Make functions. Should be number from 1 to 10, yours produces 0 to 9.  (-2)




# PROBLEM 6 (add me, multiply me - 3pts)
# Make a function which takes in two integers and RETURNS their sum AND their product.

def function(a, b):
    sum = a + b
    product = a * b
    return sum, product
print(function(10,3))

