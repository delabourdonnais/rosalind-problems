from bioIO import get_fasta_list

def is_transition(ch1, ch2):
    """returns true if mutation ch1 to ch2 is a transition"""
    return ''.join(sorted(ch1 + ch2)) in ["AG", "CT"]

def is_transversion(ch1, ch2):
    """returns true if mutation ch1 to ch2 is a transversion"""
    return ((ch1 in "AG" and ch2 in "CT")
            or (ch1 in "CT" and ch2 in "AG"))

s1, s2 = get_fasta_list("tran.fasta")
transition_count = sum([is_transition(s1[i], s2[i])
                        for i in range(len(s1))])
transversion_count = sum([is_transversion(s1[i], s2[i])
                          for i in range(len(s1))])
print float(transition_count) / transversion_count
