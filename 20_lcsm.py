from bioIO import get_fasta_list

def get_all_substrings(s, k):
    """returns a list of all substrings of length k"""
    return [s[i:i+k] for i in range(len(s)-k + 1)]

dnas = get_fastaList("lcsm.fasta")
dnas.sort(key=len)
s = dnas[0]
k = len(s)
lcs = ""
while True:
    for sub in get_all_substrings(s, k):
        found = True
        for dna in dnas[1:]:
            if dna.find(sub) == -1:
                found = False
                break
        if found:
            lcs = sub
            break
    if found:
        break
    k -= 1

print lcs
            
