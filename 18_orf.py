import re
from tables import codonTable

def get_complement(s):
    complements = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    ns = ''.join(reversed([complements[ch] for ch in s]))
    return ns

def get_protein(rna):
    protein = ""
    i = 0
    while len(codonTable[rna[i:i+3]]) == 1:
        protein += codonTable[rna[i:i+3]]
        i += 3
    return protein      

dna = ""
with open("orf.fasta", 'r') as f:
    for line in f:
        if line[0] == '>':
            continue
        dna += line.strip()
reverseDna = get_complement(dna)
rna = dna.replace('T', 'U')
reverseRna = reverseDna.replace('T', 'U')
allMatches = [re.findall("(?=(AUG(?:...)*?(?:UAA|UAG|UGA)))", s)
              for s in [rna, reverseRna]]
proteins = set([get_protein(el) for m in allMatches for el in m])
for p in proteins:
    print p

