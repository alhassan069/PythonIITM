# def sum(n):
#     ans = 0
#     for i in range(n):
#         ans = ans + (i + 1)
#     print(ans)

# sum(10)

# RECURSION


# find the sum of all the natural numbers upto a given number
def sum(n):
    # verified
    if (n == 1):
        return 1
    else:
        return n + sum(n - 1)


# compute compound interest by assuming the interest to be 10%
def compound_interest(n, p):
    # verified
    if (n == 1):
        return p * (1.1)
    else:
        return compound_interest(n - 1, p) * 1.1


# compute factorial of a number using recursion
def fact(n):
    if (n == 1):
        return 1
    else:
        return fact(n - 1) * n


print(fact(5))
