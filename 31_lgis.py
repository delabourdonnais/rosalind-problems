import bisect
import copy

with open("lgis.txt", "r") as f:
    for i, line in enumerate(f):
        n = int()
        seq = str()
        if i == 0:
            n = int(line.strip())
        elif i == 1:
            seq = [int(el) for el in line.strip().split()]
        
def lgis(seq):
    """return a list of longest increasing sequences starting from index k

    for an explanation, refer to this link
    http://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
    """
    activeLists = []
    lastElements = []
    for i, el in enumerate(seq):
        idx = bisect.bisect(lastElements, el)
        if not idx:
            #case1
            activeLists.insert(0, [el])
            lastElements.insert(0, el)
        elif idx == len(lastElements):
            #case2
            newList = copy.copy(activeLists[-1])
            newList.append(el)
            activeLists.append(newList)
            lastElements.append(el)
        else:
            #case3
            newList = copy.copy(activeLists[idx-1])
            newList.append(el)
            activeLists.insert(idx, newList)
            lastElements.insert(idx, el)
            activeLists.pop(idx+1)
            lastElements.pop(idx+1)
    return activeLists[-1]

def lgds(seq):
    negativeSeq = [-el for el in seq]
    res = lgis(negativeSeq)
    return [-el for el in res]

print " ".join([str(el) for el in lgis(seq)])
print " ".join([str(el) for el in lgds(seq)])

