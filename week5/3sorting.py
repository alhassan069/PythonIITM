# Sorting using functions

# find out the minimum element in the list
# append that to a new list
# remove the minimum from the original list l


def min_list(l):
    mini = l[0]
    for i in range(len(l)):
        if l[i] < mini:
            mini = l[i]
    return mini


def obvious_sort(l):
    x = []
    while (len(l) > 0):
        mini = min_list(l)
        x.append(mini)
        l.remove(mini)
    return x


print(obvious_sort([24, 2, 105, 9, 99]))
