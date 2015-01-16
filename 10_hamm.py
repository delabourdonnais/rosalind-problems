def get_hamming_distance(s, t):
    assert(len(s) == len(t))
    distance = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            distance +=1
            
    return distance
