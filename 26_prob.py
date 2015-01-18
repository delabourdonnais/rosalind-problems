import math

def get_prob(ch, cgContent):
    """returns the probability of getting character ch given CG-content"""
    cgContent = float(cgContent)
    if ch == 'C' or ch == 'G':
        return cgContent / 2
    elif ch == 'A' or ch == 'T':
        return (1 - cgContent) / 2
    else:
        return 0

with open("prob.txt", "rb") as f:
    for i, line in enumerate(f):
        if i == 0:
            s = line.strip()
        else:
            A = line.strip().split()

B = []
for a in A:
    B.append(round(sum([math.log(get_prob(ch, a), 10)
                  for ch in s]), 3))

print " ".join([str(b) for b in B])
