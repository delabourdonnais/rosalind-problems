from bioIO import get_fasta_list
from bioFunctions import get_complement

def get_distance(s1, s2):
    assert(len(s1) == len(s2))
    return sum([s1[i] != s2[i] for i in range(len(s1))])

def is_correct(s, dnas):
    cs = get_complement(s)
    return dnas.count(s) >= 2 or cs in dnas

dnas = get_fasta_list("corr.fasta")

correctOnes = set([dna for dna in dnas if is_correct(dna, dnas)])
incorrectOnes = {}

for dna in dnas:
    if dna in correctOnes:
        continue
    count = 0
    for s in dnas:
        cs = get_complement(s)
        if get_distance(dna, s) == 1 and s in correctOnes:
            incorrectOnes[dna] = s
        elif get_distance(dna, cs) == 1 and s in correctOnes:
            incorrectOnes[dna] = cs                
            
with open("corr.out", "w") as f:
    for k, v in incorrectOnes.iteritems():
        f.write(k + "->" + v + '\n')
