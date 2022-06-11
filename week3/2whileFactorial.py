# Lets find the factorial of a number

# n=5
# 1*2*3*4*5

# answer = 1
# answer = answer * 2
# answer = answer * 3
# answer = answer * 4
# answer = answer * 5
# answer will be 120

# now do it using while loop

print('enter a number: ')

n = int(input())

i = 1
answer = 1

while i <= n:
    answer = answer * i
    i = i + 1

print(answer)
