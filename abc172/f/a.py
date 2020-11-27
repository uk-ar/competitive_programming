#!/usr/bin/env python3
# N,M = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
# INF = float("inf")
import sys

N = int(sys.stdin.readline())
a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param

def xor(b):
    ret = 0
    for e in b:
        ret ^= e
    return ret
#return bin(ret).count("1")

if xor(a) == 0:
    print(0)
    exit()
X = xor(a[2:])





import heapq
a = [3,2,1]
heapq.heapify(a)# a == [1,2,3]
e = heapq.heappop(a) # e == 1
heapq.heappush(a, 1) # a == [1,3,2]
e = heqpq.heappushpop(a,4) # e == 1,a==[2,3,4]

st = [[1,2],[3,4]] # source dist
G = [[] for _ in range(V)]

for s,t in st:
    G[s].append(t)

visited = set()
indeg = [0]*V
ret = []
def bfs(s):
    q = collections.deque([s])
    visited.add(s)
    while q:
        u = q.popleft()
        ret.append(u)
        for v in G[u]:
            indeg[v] -= 1
            if indeg[v] == 0 and not v in visited:
                visited.add(v)
                q.append(v)

def topologicalSort_bfs():
    for a in G:
        for t in a:
            indeg[t] += 1
    #print(G,indeg)
    for i in range(V):
        if indeg[i] == 0 and not i in visited:
            bfs(i)

def dfs(s):
    #print("s:",s)
    if s in visited:
        return
    visited.add(s)
    for e in G[s]:
        dfs(e)
    ret.append(s)

def topologicalSort_dfs():
    for i in range(V):
        dfs(i)
    ret.reverse()

#topologicalSort_bfs()
topologicalSort_dfs()
print(*ret,sep='\n')
