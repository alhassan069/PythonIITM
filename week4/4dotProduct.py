# find the dot product of two lists

x = [1, 7, 3, 4]
y = [8, 6, 3, 2]
su = 0
for i in range(len(y)):
    su = su + (x[i] * y[i])
print(su)