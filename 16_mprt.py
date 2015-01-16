import re
import urllib2

def make_url(uniprotId):
    return ("http://www.uniprot.org/uniprot/"
            + uniprotId + ".fasta")

def get_protein(fasta):
    return ''.join(fasta.split('\n')[1:]).strip()

with open("mprt.txt", "rb") as f:
    ids = f.read().replace('\r', '').strip().split('\n')
    for line in ids:
        url = make_url(line)
        fasta = urllib2.urlopen(url).read()
        protein = get_protein(fasta)
        locations = ' '.join([str(m.start()+1)
                              for m in re.finditer("(?=(N[^P][ST][^P]))",
                                                   protein)])
        if locations:
            print line
            print locations
