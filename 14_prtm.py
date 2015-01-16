from tables import monoisotopicMassTable as mmt

def get_protein_weight(protein):
    return sum([mmt[ch] for ch in protein])

