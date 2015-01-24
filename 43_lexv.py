import itertools as it

letters = "ABCDEFGHIJKL"
alphabet = "HEWSIODKXRFT"
n = 3

table = {a: letters[i] for i, a in enumerate(alphabet)}
revTable = {v: k for k, v in table.iteritems()}

temp = []
for r in range(1, n+1):
    x = it.product(alphabet, repeat=r)
    temp += ["".join([table[ch] for ch in el]) for el in x]
    temp.sort()
    words = ["".join([revTable[ch] for ch in el]) for el in temp]

print '\n'.join(words)
    

