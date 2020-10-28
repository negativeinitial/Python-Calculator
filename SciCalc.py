import math as m

# ask user for input
num1 = float(input("enter a number "))
print(num1)
operation = input("enter an operation ")
print(operation)
num2 = float(input("enter a number "))
print(num2)

# define operations
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y



# results
# if operation is addition
if operation == "+":
    print(add(num1, num2))

# if operation is subtraction
elif operation == "-":
    print(subtract(num1, num2))

# if operation is multiplication
elif operation == "*":
    print(multiply(num1, num2))

# if operation is division
elif operation == "/":
    if num2 == 0:
        print("undefined")

    else:
        print(divide(num1, num2))

# ceiling
elif operation == "ceil":
    print(m.ceil(num1))

# floor
elif operation == "floor":
    print(m.floor(num1))

# factorial
elif operation == "!":
    print(m.factorial(num1))

# exponential
elif operation == "exp":
    print(m.exp(num1))

# Logarithmic
elif operation == 'log':
    result = m.log(num1)
    print(result)

elif operation == 'log10':
    result = m.log10(num1)
    print(result)

elif operation == 'log2':
    result = m.log10(num1)
    print(result)

# square root
elif operation == 'sqrt':
    result = m.sqrt(num1)
    print(result)

# trig functions
# cosine
elif operation == 'cos':
    result = m.cos(num1)
    print(result)

# sine
elif operation == 'sin':
    result = m.sin(num1)
    print(result)

# tan
elif operation == 'tan':
    result = m.tan(num1)
    print(result)

# angular conversion
elif operation == 'degrees':
    result = m.degrees(num1)
    print(result)

elif operation == 'rad':
    result = m.radians(num1)
    print(result)


else:
    print("invalid")

