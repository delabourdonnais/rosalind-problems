def mortalfib(n, m):
    s = [0] * m
    s[0] = 1
    for i in range(1, n):
        newBorn = sum(s[1:])
        for j in reversed(range(1, m)):
            s[j] = s[j - 1]
        s[0] = newBorn
    return sum(s)
