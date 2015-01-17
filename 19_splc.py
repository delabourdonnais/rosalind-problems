from bioFunctions import get_protein
dna = ""
substrings = []
with open("splc.fasta", "rb") as f:
    passedFirst = False
    s = ""
    for i, line in enumerate(f):
        if line[0] == '>':
            if s:
                if not passedFirst:
                    dna = s
                    passedFirst = True
                else:
                    substrings.append(s)
                s = ""
            continue
        s += line.strip()
    substrings.append(s)
        
for s in substrings:
    dna = dna.replace(s, "")

rna = dna.replace('T', 'U')
print get_protein(rna)
