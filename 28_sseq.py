from bioIO import get_fasta_list

s, t = get_fasta_list("sseq.fasta")
start = 0
for ch in t:
    start = s.find(ch, start) + 1
    print start,
