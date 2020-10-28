# define operations
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


#ask user for input
num1 = float(input("enter a number "))
print(num1)
operation = input("enter an operation ")
print(operation)
num2 = float(input("enter a number "))
print(num2)

#results
if operation == "+":
    print(add(num1,num2))

elif operation == "-":
    print(subtract(num1,num2))

elif operation == "*":
    print(multiply(num1,num2))

elif operation == "/":
    if num2 == 0:
        print("undefined")

    else: print(divide(num1,num2))

else: print("invalid")

