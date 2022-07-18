# 1. Write a python program to find the no of uppercase alphabets, lowercase alphabets, total characters, total words

# TEST CASES
# sentence = input("Enter the sentence")
# sentence = "Functions could have no parameters"
# sentence = "FUNCTIONS COULD HAVE NO RETURN VALUE"
# sentence = "Functions Could Have Multiple Return Statements, But The Moment The First Return Is Executed, Control Exits From The Function"
# sentence = "FUNCTIONS have to be Defined before THEY can be called, the function Call Cannot come before the DEFINITION"
# sentence = "fUNCTION CALLS COULD BE USED IN EXPRESSIONS"

import math


def upper(sen):
    upperCase = 0
    for c in sen:
        if(c.isupper()):
            upperCase += 1
    return upperCase

def lower(sen):
    lowerCase = 0
    for c in sen:
        if(c.islower()):
            lowerCase += 1
    return lowerCase


def total(sen):
    total = 0
    for c in sen:
        total+=1
    return total

def totalWords(sen):
    total = 0
    arr = sen.split(" ")
    return len(arr)

# print(upper(sentence),lower(sentence),total(sentence),totalWords(sentence))

#  2. Write a python code using functions to calculate area and perimeter of circle and rectangle

# TESTCASES

# 1. "circle" "area" 7
# 2. "circle" perimeter 7
# 3. "rectangle" "area" 15  10
# 4. rectangle perimeter 15 10
# "exit" => stop execution


pi = 22/7

def circle_area(r):
    return pi*r*r
def circle_perimeter(r):
    return 2 * pi * r
def rectangle_area(l,b):
    return l*b
def rectangle_perimeter(l,b):
    return 2*(l+b)


# MENU BASED FUNCTION

# polygon = ''
# while (polygon != "exit"):

#     print('\nPOLYGON\ncircle\nrectangle\nexit')
#     polygon = input('\nChoose the polygon type or exit:  ')
#     property = ''

#     if(polygon == 'circle'):

#         r = float(input("Enter the radius of the circle:  "))
#         while (property == ''):
#             print('\narea\nperimeter\nback')
#             property = input('Choose the property or go back:  ')

#             if (property == 'area'):
#                 cArea = circle_area(r)
#                 print('\n \x1b[6;30;42m The area of the circle is',cArea, '\x1b[0m')
#                 property = ''

#             elif (property == 'perimeter'):
#                 cPerimeter = circle_perimeter(r)
#                 print('\n \x1b[6;30;42m The perimeter of the circle is ',cPerimeter, '\x1b[0m')
#                 property = ''
            
#             elif(property == 'back'):
#                 break
#             else:
#                 print('Please select the correct property or back')
    
#     elif(polygon == 'rectangle'):

#         l = float(input("Enter the length of the rectangle:  "))
#         b = float(input("Enter the breadth of the rectangle:  "))
#         while (property == ''):
#             print('\nCHOOSE THE RECTANGLE PROPERTY\narea\nperimeter\nback')
#             property = input('Choose the property or go back:  ')

#             if (property == 'area'):
#                 rArea = rectangle_area(l,b)
#                 print('\n \x1b[6;30;42m The area of the rectangle is ',rArea, '\x1b[0m')
#                 property = ''

#             elif (property == 'perimeter'):
#                 rPerimeter = rectangle_perimeter(l,b)
#                 print(' \n \x1b[6;30;42m The perimeter of the rectangle is ', rPerimeter,'\x1b[0m')
#                 property = ''

#             elif(property == 'back'):
#                 break
#             else:
#                 print('Please select the correct property or back')

#     elif(polygon == 'exit'):
#         break
#     else:
#         print('Please select the correct polygon type or exit')



# WRITE A PYTHON CODE USING FUNCTIONS WHICH CHECKS WHETHER THE INPUT COORDINATES FORM A TRIANGLE OR NOT

# STEP 1 using Triangle property

def distance(x1,y1,x2,y2):
    distance = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    return distance

# def isTriangle(a,b,c):
#     # getting coordinates
#     x1 = a[0]
#     y1 = a[1]
#     x2 = b[0]
#     y2 = b[1]
#     x3 = c[0]
#     y3 = c[1]
#     # finding distance 
#     d1 = distance(x1,y1,x2,y2)
#     d2 = distance(x2,y2,x3,y3)
#     d3 = distance(x3,y3,x1,y1)
#     # checking the biggest distance
#     if (d1 > d2):
#         if(d1>d3):
#             final(d1,d2,d3)
#         else:
#             final(d3,d1,d2)
#     elif(d2>d3):
#         final(d2,d1,d3)
#     else:
#         final(d3,d1,d2)

    

def final(max,a,b):
    if((a+b)>max):
        print('Triangle')
    else:
        print('Not Triangle')
    
# isTriangle([0,0],[0,1],[1,0])
# isTriangle([-3,-5],[-7,10],[0,0])
# isTriangle([1,2],[1,10],[5,2])
# isTriangle([1,1],[2,2],[3,3])
# isTriangle([2,3],[3,2],[2,3])
# isTriangle([0,0],[10,0],[0,0.0001])

# STEP 2 USING SLOPE PROPERTY


def isTriangle(a,b,c):
    # getting coordinates
    x1 = a[0]
    y1 = a[1]
    x2 = b[0]
    y2 = b[1]
    x3 = c[0]
    y3 = c[1]
    # finding slope
    s1 = slope(x1,y1,x2,y2)
    s2 = slope(x2,y2,x3,y3)
    if (s1 != s2):
        print("Triangle")
    else:
        print("Not Triangle")

# finding slope of a line
def slope(x1,y1,x2,y2):
    if(x1==x2):
        return math.inf
    else:
        return (y2-y1)/(x2-x1)


isTriangle([0,0],[0,1],[1,0])
isTriangle([-3,-5],[-7,10],[0,0])
isTriangle([1,2],[1,10],[5,2])
isTriangle([1,1],[2,2],[3,3])
isTriangle([2,3],[3,2],[2,3])
isTriangle([0,0],[10,0],[0,0.0001])