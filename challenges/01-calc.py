# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

#First function is for addition
def addition (x, y):
    return x + y

#Next for subtraction
def subtraction (x, y):
    return x - y

#Now multiplication
def multiplication (x, y):
    return x * y

#and now division
def division(x, y):
    return x / y

print("Select your operation.\n1.) Addition\n 2.) Subtraction\n 3.) Multiplication\n 4.) Division")

while True:
    #take input from the user
    choice = input ("Enter choice(1/2/3/4): ")

    #check if the choice is permissable, 1-4
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", addition(num1,num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtraction(num1,num2))
        elif choice == '3':
            print(num1, "x", num2, "=", multiplication(num1,num2))
        elif choice == '4':
            print(num1, "/", num2, "=", division(num1,num2))
        #now we check if there's another calculation
        next_calc = input("Are we going to do another one? (yes/no): ")
        if next_calc == "no":
            break
    
    else:
        print("Invalid input")