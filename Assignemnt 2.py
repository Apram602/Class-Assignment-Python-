def subtraction(x,y):
    c=x-y
    print("Answer=",c)

def addition(x,y):
    c=x+y
    print("Answer=",c)

def multiply(x,y):
    c=x*y
    print("Answer=",c)

def divide(x,y):
    c=x/y
    print("Answer=",c)

def takeInput():
    a = int(input("Number One = "))
    b = int(input("Number Two = "))
    op = input("operator = ")
    return a, b, op

def displayResult(a, b, op):
    if op == "+":
        addition(a, b)
    elif op == "-":
        subtraction(a, b)
    elif op == "*":
        multiply(a, b)
    elif op == "/":
        divide(a, b)
    else:
        print("Not a valid operator")


Number_One , Number_Two, operator = takeInput()
displayResult(Number_One, Number_Two, operator)
