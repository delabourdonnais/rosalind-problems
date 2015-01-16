def fibnk(n, k):
    s = [1, 0]
    for i in range(1, n):
        adults = s[1] + s[0]
        youngs = s[1] * k
        s = [youngs, adults]
    return sum(s)
