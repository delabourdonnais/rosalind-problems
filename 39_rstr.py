def get_match_probability(x, dna):
    probs = {'C': x / 2, 'G': x / 2, 'A': (1 - x) / 2, 'T': (1 - x) / 2}
    return reduce(lambda x, y: x*y, [probs[ch] for ch in dna], 1)

def get_probability(N, x, dna):
    p = get_match_probability(x, dna)
    return 1 - ((1 - p) ** N)
