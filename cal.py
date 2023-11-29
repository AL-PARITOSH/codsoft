def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    if(y==0):
        return "Zero Division Error"
    else:
        return x/y

while True:
    print("Options: ")
    print("Enter 'add' for add of two numbers ")
    print("Enter 'sub' for subtraction of two numbers ")
    print("Enter 'mul' for product of two numbers ")
    print("Enter 'div' for division of two numbers ")
    print("Enter 'quit' to end the program ")

    user_input=input(": ")

    if(user_input=="quit"):
        break
    elif(user_input in("add","sub","mul","div")):
        x=float(input("Enter the 1st number :"))
        y=float(input("Enter the 2nd number :"))

        if(user_input=="add"):
           print("Result: ",add(x,y))
        elif(user_input=="sub"):
           print("Result: ",sub(x,y))
        elif (user_input == "mul"):
           print("Result: ", mul(x, y))
        elif (user_input == "div"):
           print("Result: ", div(x, y))
    else:
        print("Enter an invalid input")