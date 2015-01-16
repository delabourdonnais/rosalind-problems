def get_gc(dna):
    s = sum([ch == 'G' or ch == 'C' for ch in dna])
    return 100 * (float(s) / len(dna))

def get_max(fileName):
    scores = []
    dnaId = ""
    dnaString = ""
    with open(fileName, 'r') as f:
        for line in f:
            if line[0] == '>':
                if dnaId and dnaString:
                    scores.append((get_gc(dnaString),
                                   dnaId))
                dnaId = line[1:].strip()
                dnaString = ""
            else:
                dnaString += line.strip()
        scores.append((get_gc(dnaString), dnaId))
    
    scores.sort()
    print scores[-1][1]
    print scores[-1][0]
    
