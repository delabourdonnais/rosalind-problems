from bioIO import get_fasta_list

rna = get_fasta_list("mmch.fasta")[0]

def count_mmch(rna):
    aucount1, aucount2 = sorted([rna.count('A'), rna.count('U')])
    cgcount1, cgcount2 = sorted([rna.count('C'), rna.count('G')])
    res = 1
    for i in range(aucount1):
        res *= (aucount2 - i)
    for i in range(cgcount1):
        res *= (cgcount2 - i)
    return res

print count_mmch(rna)
