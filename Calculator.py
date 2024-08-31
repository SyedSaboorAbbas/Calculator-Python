# Lets make a calculator


# Function Of Addition

def add(a,b):
    sum=a+b
    print("Sum of Two number:",sum)
    return sum

# add(number1,number2)

# Function Of Subtraction

def sub(a,b):
    sub=a-b
    print("Subtract of Two number:",sub)
    return sub

# sub(number1,number2)

# Function Of Multiplication

def mul(a,b):
    mul=a*b
    print("Multiply of Two number:",mul)
    return mul

# mul(number1,number2)

# Function Of Division

def div(a,b):
    div=a/b
    print("Sum of Two number:",div)
    return div

# div(number1,number2)

#Condtional Statement

while(True):
    # take 2 numbers from from user
    number1=int(input("Enter number 1:"))
    number2=int(input("Enter number 2:"))

    print("Press A for Addition\n Press S for Subtraction\n Press M for Multiply\nPress D for Divison")

    press=input("Press the Word")


    if(press=="A"):
        add(number1,number2)
    elif(press=="S"):
        sub(number1,number2)
    elif(press=="M"):
        mul(number1,number2)
    elif(press=="D"):
        div(number1,number2)
    else:
        print("Invalid input, please try again.")
        break

    

