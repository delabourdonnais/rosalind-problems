from bioIO import get_fasta_list

def get_superstring(s1, s2):
    k = 1
    while s1.find(s2[:k]) != -1:
        k += 1
    return s1 + s2[k-1:]

def is_pair(s1, s2):
    n = len(s1)
    return s2.find(s1[n/2:]) != -1

strings = get_fasta_list("long.fasta")
chain = {}
reversedChain = {}
for s1 in strings:
    for s2 in strings:
        if s1 == s2:
            continue
        if is_pair(s1, s2):
            chain[s1] = s2
            reversedChain[s2] = s1

sortedStrings = []
for s in strings:
    if s not in reversedChain:
        node = s
        sortedStrings.append(node)
        break
    
while node in chain:
    node = chain[node]
    sortedStrings.append(node)

print reduce(get_superstring, sortedStrings, "")
