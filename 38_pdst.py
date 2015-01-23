from bioIO import get_fasta_list

dnas = get_fasta_list("pdst.fasta")

def get_distance(s1, s2):
    assert(len(s1) == len(s2))
    errors = sum([s1[i] != s2[i] for i in range(len(s1))])
    return float(errors) / len(s1)

with open("pdst.out", "w") as f:
    for dna in dnas:
        res = " ".join([str(get_distance(dna, s)) for s in dnas])
        f.write(res+'\n')
