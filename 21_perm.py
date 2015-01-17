import itertools as it

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def print_all_permutations(n):
    """print permutations of the sequence 1 2 ... n"""
    print factorial(n)
    x = it.permutations(range(1, n+1))
    for el in x:
        print ' '.join([str(d) for d in el])

