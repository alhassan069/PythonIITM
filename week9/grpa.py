# GRPA1:


def get_freq(filename):
    f = open(filename, 'r')
    d = {}
    l = f.readline().strip('\n')

    while (l != ''):
        if (l in d):
            d[l] += 1
        else:
            d[l] = 1
    l = f.readline().strip('\n')

    return d


# GRPA 2


def length(file):
    f = open(file, 'r')
    c = 1
    s = f.readline().strip('\n')
    while (s != ''):
        s = f.readline().strip('\n')
        c += 1
    return c - 1


def relation(file1, file2):
    f1 = length(file1)
    f2 = length(file2)
    g1 = open(file1, 'r')
    g2 = open(file2, 'r')
    flag = 0
    for i in range(f1):
        if ((g1.readline()).strip('\n') != (g2.readline()).strip('\n')):
            flag = 1
            break
    if (flag == 1):
        ans = 'No Relation'
    else:
        if (f1 == f2):
            ans = 'Equal'
        if (f1 < f2):
            ans = 'Subset'
    return ans


# GRPA 3
def get_goals(filename, country):
    import pandas as pd
    x = pd.read_csv(filename)
    if (x[x['Country'] == country].shape[0] == 0):
        return (-1, -1)
    else:
        t = (x[x['Country'] == country].shape[0],
             x[x['Country'] == country]['Goals'].sum())
        return t


# GRPA 4


def num_to_words(mat):
    n = len(mat)
    f = open('words.csv', 'w')
    d = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten'
    }

    for i in range(n):
        for j in range(n):
            s = d[mat[i][j]]
            f.write(s)
            if (j < n - 1):
                f.write(',')
        if (i < n - 1):
            f.write('\n')


# GRPA 3 ***************


def get_goals(filename, country):
    f = open(filename, 'r')
    l = f.readlines()[1:]
    c = -1
    g = -1
    for i in l:
        if country in i:
            t = i.split(',')
            if c == -1:
                c = 1
                g = int(t[2])
            else:
                c += 1
                g += int(t[2])
    f.close()
    return ((c, g))
