def add(a, b):
    ans = a + b
    return ans


# print(ans)

# add(7, 8)


def discount(cost, d):
    ans = cost - ((d / 100) * cost)
    print(ans)


# discount(add(12453, 78), 1.22)

print('Enter the cost price')
x = int(input())

print('Enter the discount')
y = int(input())

print('The final discount is: ', discount(x, y))
