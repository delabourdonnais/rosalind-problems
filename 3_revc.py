def get_complement(s):
    complements = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    ns = ''.join(reversed([complements[ch] for ch in s]))
    return ns
