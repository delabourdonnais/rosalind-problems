with open("tree.txt", "rb") as f:
    k = 0
    for i, line in enumerate(f):
        if i == 0:
            n = int(line.strip())
            continue
        k += 1

print (n - 1) - k
