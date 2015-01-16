dnas = {}
with open("cons.fasta", "rb") as f:
    dnaId = ""
    dnaString = ""
    #content = f.read().replace("\r", "").strip().split('\n')
    for line in f:
        if line[0] == ">":
            if dnaId and dnaString:
                dnas[dnaId] = dnaString
            dnaString = ""
            dnaId = line[1:].strip()
        else:
            dnaString += line.strip()
    dnas[dnaId] = dnaString
    n = len(dnaString)

def get_consensus(profile):
    na = 'ACGT'
    n = len(profile[0])
    idxes = [max([(profile[i][j], i) for i in range(4)])
     for j in range(n)]
    return ''.join([na[el[1]] for el in idxes])

naMapping = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
profile = [[0 for i in range(n)] for j in range(4)]

for dna in dnas.itervalues():
    for i, ch in enumerate(dna):
        profile[naMapping[ch]][i] += 1

print get_consensus(profile)
for l in 'ACGT':
    idx = naMapping[l]
    print l + ":",
    print ' '.join([str(el) for el in profile[idx]])
