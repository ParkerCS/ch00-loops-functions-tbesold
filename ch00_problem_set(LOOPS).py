# LOOPS (22pts TOTAL)
import random
# PROBLEM 1 (Fibonacci - 4pts)
## The Fibonacci sequence is a sequence of numbers that starts with 1, followed by 1 again.
# Every next number is the sum of the two previous numbers.
# I.e., the sequence starts with 1, 1, 2, 3, 5, 8, 13, 21,...
# Write a program that calculates and prints the Fibonacci sequence
# until the numbers get higher than 1000.

number = 0
number_2 = 1
number_3 = 1

while number <= 1000:
    number_3 = number + number_2
    number += number_3

    print(number_3)

#stuck here not sure what to do





# PROBLEM 2 (Number Guessing Game - 6pts)
# Write a program that takes a random integer between 1 and 1000
# The program then asks the user to guess the number.

# It might be wise, for testing purposes, to also display the number that the
# program randomly picks, until you are sure that the program works correctly

random_int = random.randrange(1,1001)
for i in range(500):
    user_guess = int(input("Guess a number between one and a thousand: "))
    if user_guess > random_int:
        print("your guess is higher than the number. Try again")
    if user_guess < random_int:
        print("your guess is lower than the number. Try again")
    if user_guess == random_int:
        print("You guessed correctly!")
        break





# PROBLEM 3 (Dice Hi-Low - 6pts)
# You roll five six-sided dice, one by one.
# How big is the probability that the value of each die
# is greater than or equal to the value of the previous die that you rolled?

# probability of success using a simulation of a large number of trials.

success = 0
rolls = 100000
for i in range(rolls):
    a = random.randrange(1,7)
    b = random.randrange(1,7)
    c = random.randrange(1,7)
    d = random.randrange(1,7)
    e = random.randrange(1,7)
    if a <= b and b <= c and c <= d and d <= e:
        success += 1
#print(success/rolls)   not sure why this doesnt work
print("of", rolls, "rolls", success, "were successful")









# PROBLEM 4 (Number Puzzler - 6pts)
# A, B, C, and D are all different digits.
# The number DCBA is equal to 4 times the number ABCD.
# What are the digits?
# Note: to make ABCD and DCBA conventional numbers, neither A nor D can be zero.
# Use a quadruple-nested loop to solve.

for a in range(1,10):
    for b in range(10):
        for c in range(10):
            for d in range(1,10):
                ABCD = int(str(a) +str(b) + str(c) + str(d))
                DCBA = int(str(d) + str(c) + str(b) + str(a))
                if DCBA == 4 * ABCD:
                    print("ABCD is", a, b, c, d)
                    print("DCBA is", d, c, b, a)






