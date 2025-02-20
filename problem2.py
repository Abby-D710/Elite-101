#UNDERSTAND:
#  This program will find the factorial of a number
# Input: The number we need to find the factorial of
# Ouput: Factorial of the given number
# Edge case: User gives a negative number, therefore we must tell the user it's not possible

# CLUES: 
# We will need to use a for loop, as we have to keep multiplying until we've hit the number.
# We will need to use if/else to take care of our edge case (if user gives n < 0)

# ASSEMBLE:
# ask user for the number, use int(input("...."))
# set the factorial to 1 as a starting point, we will add to it afterwards
# if the number is less than 0 --->
#   print to the user it's not possible.
# else  if the number is greater than 0 --->
#   for (1 ---> num + 1):
#       factorial will be updated to be multiplied by the loop #
#   print that the factorial of the number

#SOLVE:
# To take input from the user
num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
else:
   for i in range(1,num+1):
       factorial = factorial*i
   print(f"The factorial of {num} is {factorial}")

#EXAMINE:
# code works well, however we could try to improve it by checking to see if the number is a valid
# string integer. We could also return to the user to enter a new number after providing a number 
# in the negatives.
