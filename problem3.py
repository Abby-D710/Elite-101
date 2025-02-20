
number = input("Hello! Please type in a number, and we will tell you if it is even! ")

def evenOrNot(n):
    if n % 2 == 0:
        print("True")
    else:
        print("False")

try:
     number = int(number)
except ValueError:
    print("Invalid Input, please type a number.")

evenOrNot(number)