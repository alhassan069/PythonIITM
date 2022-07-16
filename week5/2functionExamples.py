# Lets write a few functions on list.


def list_min(l):
    mini = l[0]
    for i in range(len(l)):
        if (l[i] < mini):
            mini = l[i]
    return mini


l = [1, 5, -6, 9, 3, 2, 4, 5, 6, 89]

# print(list_min(l))


def list_max(l):
    maxi = l[0]
    for i in range(len(l)):
        if (l[i] > maxi):
            maxi = l[i]
    return maxi


# print(list_max(l))

z = [2, 4, 6, 8, 10]


def append_before(a, b):
    newL = []
    for i in range(len(b)):
        newL.append(b[i])
    for i in range(len(a)):
        newL.append(a[i])
    return newL


# print(append_before(l, z))


def find_average(l):
    sum = 0
    for i in range(len(l)):
        sum = sum + l[i]
    return sum / len(l)


print(find_average([2, 2, 2, 2, 2, 2, 2]))
