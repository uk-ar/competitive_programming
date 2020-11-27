#!/usr/bin/env python3
# N,M = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
# INF = float("inf")
G = [[] for _ in range(V)]

for s,t in st: # t depends on s
    G[s].append(t)

def dfs(s):
    #print("s:",s)
    if s in visited:
        return
    for e in G[s]:
        dfs(e)
    ret.append(s)
    visited.add(s)

def topologicalSort_dfs():
    for i in range(V):
        dfs(i)
    ret.reverse()
#st = [[0,1],[0,2],[1,2],[2,3]]
G = {i:[] for i in range(V)}

for s,t in st:
    G[s].append(t)

def dfs_cycle(s):
    act.add(s)
    visited.add(s)
    #print(s,act,visited,G)
    if not s in G:
        act.remove(s)
        return
    for e in G[s]:
        #print(s,e,act)
        if e in act:
            global bad
            bad = True
            return
        elif not e in visited:
            dfs_cycle(e)
    act.remove(s)

bad = False
visited = set()
act = set()
for s,_ in st:
    if not s in visited:
        dfs_cycle(s)
if bad:
    print(1)#has cycle
else:
    print(0)
G = [[] for _ in range(V)]

for s,t in st: # t depends on s
    G[s].append(t)

ret = []
visited = set()
visiting = set()
self.is_cycle = False
