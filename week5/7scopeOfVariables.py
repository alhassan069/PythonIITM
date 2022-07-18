def myFunction():
    global x
    x = x *2
    print("value of x in function 1 is ",x)


x = 5

print("Value of x before function call is ",x)

myFunction()


print("Value of x after function call is ", x)