# 1 find the factorial of a given number

# num = int(input('Enter a number: '))

# fact = 1

### while loop
# if (num < 0):
#     print("Not Defined")
# else:
#     while num > 0:
#         fact = fact * num
#         num = num - 1
#     print(fact)
### for loop
# if (num < 0):
#     print("Not Defined")
# else:
#     for i in range(num, 0, -1):
#         fact = i * fact
#     print(fact)

# 2 find the number of digits in a given number

# num = abs(int(input('Enter a number: ')))

### mathematically
# digits = 1
# while num > 10:
#     num = num // 10
#     digits = digits + 1
# print(digits)

### using string and for loop

# strNum = str(num)
# digits = 0
# for c in strNum:
#     digits = digits + 1
# print(digits)

#  3 reverse the digits in a given number

# num = int(input('enter a number'))

# strNum = str(abs(num))
# rev = ''
# for c in strNum:
#     rev = c + rev
# if num >= 0:
#     print(int(rev))
# else:
#     print('-' + rev)

# find if a number a pallindrome

# num = int(input('enter a num'))

# absStrNum = str(abs(num))

# rev = ''
# for c in absStrNum:
#     rev = c + rev
# if (num < 0):
#     rev = '-' + rev
# if (num == int(rev)):
#     print('Pallindrome')
# else:
#     print('Not a pallindrome')
