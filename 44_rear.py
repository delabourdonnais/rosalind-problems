from collections import deque
import heapq

def get_reversal_distance(start, goal):
    """start and goal are two lists representing permutations"""
    start = list(start)
    count = 0
    for i in reversed(range(len(goal))):
        if goal[i] != start[i]:
            j = start.index(goal[i])
            start[j:i+1] = [el for el in reversed(start[j:i+1])]
            count += 1
    return count

def get_partial_reversal(node, i, j):
    """reverses the sequence between i and j"""
    copy = list(node)
    copy[i:j+1] = [el for el in reversed(copy[i:j+1])]
    return copy

def bfs(start, goal):
    """solves the problem using breadth first search"""
    queue = deque([start])
    visited = set([tuple(start)])
    parents = {tuple(start): -1}
    while queue:
        node = queue.popleft()
        if node == goal:
            return get_path_length(parents, goal)
        for i in range(len(start) - 1):
            for j in range(i+1, len(start)):
                follower = get_partial_reversal(node, i, j)
                if tuple(follower) not in visited:
                    queue.append(follower)
                    visited.add(tuple(follower))
                    parents[tuple(follower)] = node
                    

def ucs(start, goal):
    """solves the problem using uniform cost search"""
    heap = [(1, start)]
    visited = set([tuple(start)])
    parents = {tuple(start): -1}
    while heap:
        node = heapq.heappop(heap)
        visited.add(tuple(node[1]))
        if node[1] == goal:
            return get_path_length(parents, goal)
        for i in range(len(start) - 1):
            for j in range(i+1, len(start)):
                nextNode = get_partial_reversal(node[1], i, j)
                nextCost = get_reversal_distance(nextNode, goal)
                follower = (nextCost, nextNode)
                if tuple(nextNode) not in visited:
                    heapq.heappush(heap, follower)
                    parents[tuple(nextNode)] = node[1]

def get_path_length(parents, goal):
    count = 0
    node = tuple(goal)
    while(parents[node] != -1):
        node = tuple(parents[node])
        count += 1
    return count

with open("rear.txt", "r") as f:
    res = []
    for i, line in enumerate(f):
        if i % 3 == 0:
            start = [int(el) for el in line.strip().split()]
        elif i % 3 == 1:
            goal = [int(el) for el in line.strip().split()]
            res.append(ucs(start, goal))

print " ".join([str(el) for el in res])
