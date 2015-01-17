from bioFunctions import get_complement
from bioIO import get_fasta_list

dna = get_fastaList("revp.fasta")[0]

def get_all_substrings(s, k):
    """returns a list of all substrings of length k"""
    return [s[i:i+k] for i in range(len(s)-k + 1)]

def is_revp(s):
    return s == get_complement(s)

for i in range(4, 13):
    for k, sub in enumerate(get_all_substrings(dna, i)):
        if is_revp(sub):
            print k + 1, i
        
