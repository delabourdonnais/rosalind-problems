def get_fasta_dict(fileName):
    """reads a fasta file and returns a dictionary of id:string records"""
    records = {}
    with open(fileName, 'rb') as f:
        recordId = ""
        recordString = ""
        for line in f:
            if line[0] == ">":
                if recordId and recordString:
                    records[recordId] = recordString
                recordId = line[1:].strip()
                recordString = ""
            else:
                recordString += line.strip()
        records[recordId] = recordString
    return records

def get_fasta_list(fileName):
    """reads a fasta file and returns a list of strings"""
    strings = []
    with open(fileName, 'rb') as f:
        s = ""
        for line in f:
            if line[0] == ">":
                if s:
                    strings.append(s)
                    s = ""
                continue
            s += line.strip()
        strings.append(s)
    return strings


            
    
