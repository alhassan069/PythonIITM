# grpa 1
def reverse(input_list):
    if len(input_list) == 0:
        return input_list
    else:
        return [input_list[-1]] + reverse(input_list[:-1])


# grpa 2
def linear(P, Q, K):
    if (len(P) != len(Q)):
        return False
    if (P == []):
        return True
    if (P[0] != K * Q[0]):
        return False
    else:
        P.remove(P[0])
        Q.remove(Q[0])
        return (linear(P, Q, K))


# Grpa 3:


def collatz(n):
    if (n % 2 == 0):
        result = (n // 2)
    else:
        result = (3 * n) + 1
    while (result != 1):
        return (1 + collatz(result))
    return (1)


# Grpa 4:


def steps(n):
    if (n < 4):
        initial = [1, 2, 4]
        return initial[n - 1]
    else:
        return steps(n - 1) + steps(n - 2) + steps(n - 3)


# Grpa 5:


def ancestry(P, present, past):
    l = []
    if (P[present] == past):
        l.append(present)
        l.append(past)
        return (l)
    else:
        l.append(present)
        pre = P[present]
        pa = past
        return (l + ancestry(P, pre, pa))
