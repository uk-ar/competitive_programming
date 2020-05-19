# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# a = [sys.stdin.readline() for s in range(n)]
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
import sys
import collections
import heapq
T = int(sys.stdin.readline())

def dfs_dag(s):
    #print(s)
    if s in d_visited:
        return
    d_visited.add(s)
    if not s in P:
        ret.append(s)
        return
    for e in P[s]:
        dfs_dag(e)
    ret.append(s)

def dfs_cycle(s):
    act.add(s)
    visited.add(s)
    if not s in P:
        act.remove(s)
        return
    for e in P[s]:
        if e in act:
            global bad
            bad = True
            return
        elif not e in visited:
            dfs_cycle(e)
    act.remove(s)

def dfs(s):
    # if s in visited:
    #     return
    act.add(s)
    visited.add(s)
    #print(s,act,visited,P)
    if not s in P:
        act.remove(s)
        ret.append(s)
        return
    for e in P[s]:
        if e in act:#and s!=e
            global bad
            bad = True
        elif not e in visited:
            dfs(e)
    act.remove(s)
    ret.append(s)

for t in range(T):
    R,C = map(int,sys.stdin.readline().split())
    GRID = list(sys.stdin.readline().rstrip() for _ in range(R)) # multi line with multi param
    P = {}
    #print(GRID)
    tv = set()
    v = [set(GRID[0][c]) for c in range(C)]
    for r in range(R):
        for c in range(C):
            tv.add(GRID[r][c])
        if r:
            for c in range(C):
                if GRID[r-1][c] != GRID[r][c]:
                    if not GRID[r-1][c] in P: P[GRID[r-1][c]]=list()
                    P[GRID[r-1][c]].append(GRID[r][c])
    visited = set()
    act = set()
    bad = False
    for i in tv:
        if not i in visited:
            dfs_cycle(i)
    if bad:
        print("Case #{}: {}".format(t+1,-1))
        continue
    visited = set()
    ret = []
    for i in tv:
        if not i in visited:
            dfs(i)
    # if bad:
    #     print("Case #{}: {}".format(t+1,-1))
    #     continue
    # print("Case #{}: {}".format(t+1,"".join(ret)))
    print("Case #{}: {}".format(t+1,"".join(ret)))
    # ret = []
    # d_visited = set()
    # for i in P.keys():
    #     dfs_dag(i)
