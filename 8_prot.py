from tables import codonTable

def translate_to_protein(rna):
    protein = ""
    codon = ""
    for ch in rna:
        codon += ch
        if len(codon) == 3:
            aminoacid = codon_table[codon]
            if len(aminoacid) != 1:
                break
            protein += aminoacid
            codon = ""
    return protein
