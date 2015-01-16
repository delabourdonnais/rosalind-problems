import re
from tables import codonTable

dna = ""
with open("orf.fasta", 'r') as f:
    for line in f:
        if line[0] == '>':
            continue
        dna += line.strip()
rna = dna.replace('T', 'U')
allMatches = re.findall("(?=(AUG.*?(?:UAA|UAG|UGA)))", rna)
print allMatches
