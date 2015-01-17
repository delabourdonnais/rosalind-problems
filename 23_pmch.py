from bioIO import get_fasta_list

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def get_perfect_matchings(rna):
    """return the number of perfect matchings
        of the graph of basepair edges"""
    k = rna.count('A')
    j = rna.count('C')
    return factorial(k) * factorial(j)
rna = get_fasta_list("pmch.fasta")[0]
print get_perfect_matchings(rna)
