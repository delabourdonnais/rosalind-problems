from bioIO import get_fasta_list

dna = get_fasta_list("kmp.fasta")[0]

def get_failure(s):
    failure = [0]
    m = len(s)
    k = 0
    for q in range(1, len(s)):
        while k > 0 and s[k] != s[q]:
            k = failure[k-1]
        if s[k] == s[q]:
            k += 1
        failure.append(k)
    return failure

res =  " ".join([str(el) for el in get_failure(dna)])
with open("kmp.out", "w") as f:
    f.write(res)
