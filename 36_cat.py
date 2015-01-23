from bioIO import get_fasta_list

rna = get_fasta_list("cat.fasta")[0]

cats = {'': 1}
def cat(rna):
    """returns the desired quantity for the cat rosalind problem"""
    global cats
    assert(len(rna) % 2 == 0)
    if rna in cats:
        return cats[rna]
    n = len(rna) / 2
    pairs = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}
    res = 0
    for k in range(n):
        if rna[2*k+1] == pairs[rna[0]]:
            res += cat(rna[1:2*k+1]) * cat(rna[2*k+2:2*n])
    cats[rna] = res
    return res

print cat(rna)%1000000
