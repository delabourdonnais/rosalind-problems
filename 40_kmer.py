import itertools as it
from bioIO import get_fasta_list

dna = get_fasta_list("kmer.fasta")[0]
n = len(dna)
counts = {}
for i in range(n-3):
    counts[dna[i:i+4]] = 1 + counts.get(dna[i:i+4], 0)

x = it.product("ACGT", repeat=4)
res = " ".join([str(counts.get(''.join(el), 0)) for el in x])
with open("kmer.out", "w") as f:
    f.write(res)
    
