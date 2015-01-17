def pper(n, k):
    """returns number of partial permutations modulo X"""
    X = 1000000
    res = reduce(lambda x, y: (x*y)%X, [n-i for i in range(k)], 1)
    return res
