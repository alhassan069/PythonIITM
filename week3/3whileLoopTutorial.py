# 1 factorial finding

# print("Enter a number to find the tutorial.")

# num = int(input())
# if (num < 0):
#     print('Not Defined')
# else:

#     fact = 1
#     i = 1
#     while num > i:
#         fact = fact * num
#         num = num - 1
#     print(fact)

###################################################################
# 2 find number of digits in the given number

# num = abs(int(input()))

# digits = 1

# while num > 9:
#     num = num // 10
#     digits = digits + 1
#     print(num)
# print(digits)

###################################################################
# 3 reverse the digits in the given number

# num = int(input('enter a number: '))
# absNum = abs(num)
# rev = absNum % 10
# absNum = absNum // 10

# while (absNum > 0):
#     r = absNum % 10
#     absNum = absNum // 10
#     rev = rev * 10 + r

# if num >= 0:
#     print(rev)
# else:
#     print(rev - 2 * rev)

##################################################################
#  4. check if the number is pallindrome or not

num = int(input('enter a number: '))
absNum = abs(num)
rev = absNum % 10
absNum = absNum // 10

while (absNum > 0):
    r = absNum % 10
    absNum = absNum // 10
    rev = rev * 10 + r

if num < 0:
    rev = rev - 2 * rev
if num == rev:
    print("Pallindrome")
else:
    print("Not Pallindrome")