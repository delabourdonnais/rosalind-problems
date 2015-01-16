dnas = {}
with open("grph.fasta", "rb") as f:
    dnaId = ""
    dnaString = ""
    for line in f:
        if line[0] == '>':
            if dnaId and dnaString:
                dnas[dnaId] = dnaString
            dnaId = line[1:].strip()
            dnaString = ""
        else:
            dnaString += line.strip()
    dnas[dnaId] = dnaString

for k1, v1 in dnas.iteritems():
    for k2, v2 in dnas.iteritems():
        if k1 == k2:
            continue
        if v1[-3:] == v2[:3]:
            print k1, k2
