import itertools as it

def print_strings(alphabet, n):
    """prints strings of length n from alphabet in lexicographical order"""
    alphabet = alphabet.split()
    x = it.product(alphabet, repeat=n)
    for el in x:
        print "".join(el)
    
