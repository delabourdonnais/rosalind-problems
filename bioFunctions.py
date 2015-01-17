from tables import codonTable

def get_complement(s):
    complements = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    ns = ''.join(reversed([complements[ch] for ch in s]))
    return ns

def get_protein(rna):
    if len(rna) % 3 != 0:
        rna = rna[:-len(rna)%3]
    protein = ""
    i = 0
    while len(codonTable[rna[i:i+3]]) == 1:
        protein += codonTable[rna[i:i+3]]
        i += 3
    return protein
