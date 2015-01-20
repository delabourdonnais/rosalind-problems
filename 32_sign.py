import itertools as it

def factorial(n):
    if not n:
        return 1
    return n * factorial(n-1)

def print_signed_permutations(n):
    print factorial(n) * (2 ** n)
    x = it.permutations(range(1, n+1))
    N = 2 ** n
    for p in x:
        for i in range(N):
            signs = [2 * ((i & (1 << j)) > 0) - 1 for j in range(n)]
            print " ".join([str(p[idx] * signs[idx])
                            for idx in range(n)])
