from tables import codonTable

revCodonCount = {}
for k, v in codonTable.iteritems():
    revCodonCount[v] = (revCodonCount.get(v, 0)
                          + 1)

def get_nb_rnas(protein):
    count = 1
    for ch in protein:
        count *= revCodonCount[ch]
        count %= 1000000
    return (3 * count) % 1000000
