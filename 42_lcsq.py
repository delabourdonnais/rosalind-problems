import sys
from bioIO import get_fasta_list

sys.setrecursionlimit(10000)
lcs = {}

def lcsq(s, t):
    """returns the longest common subsequence of s and t"""
    global lcs
    res = ""
    if (s, t) in lcs:
        return lcs[(s, t)]
    if s == "" or t == "":
        return ""
    if s[-1] == t[-1]:
        res = lcsq(s[:-1], t[:-1]) + s[-1]
    else:
        res = max(lcsq(s[:-1], t), lcsq(s, t[:-1]), key=len)
    lcs[(s, t)] = res
    return res

s, t = get_fasta_list("lcsq.fasta")
print lcsq(s, t)
