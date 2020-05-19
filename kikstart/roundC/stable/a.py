# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# a = [sys.stdin.readline() for s in range(n)]
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
import sys
import collections
import heapq
T = int(sys.stdin.readline())

def dfs(s):
    global res
    if s in g_visited:
        return
    if s in P:
        g_visited.add(s)
        l_visited.add(s)
        for e in P[s]:
            if e in l_visited:
                res = False
            dfs(e)
    ret.append(s)

for t in range(T):
    R,C = map(int,sys.stdin.readline().split())
    GRID = list(sys.stdin.readline().rstrip() for _ in range(R)) # multi line with multi param
    P = {}
    res = True
    #print(GRID)
    v = [set(GRID[0][c]) for c in range(C)]
    for c in range(C):
        P[GRID[0][c]] = set()
    for r in range(R-1):
        for c in range(C):
            v[c].add(GRID[r][c])
            if GRID[r][c] != GRID[r+1][c]:
                if GRID[r+1][c] in v[c]:
                    res = False
                if not GRID[r][c] in P:
                    P[GRID[r][c]] = set()
                P[GRID[r][c]].add(GRID[r+1][c])
    ret = []
    #print(P)
    g_visited = set()
    for i in P.keys():
        l_visited = set()
        dfs(i)
    #print(ret,res)
    if res:
        print("Case #{}: {}".format(t+1,"".join(ret)))
    else:
        print("Case #{}: {}".format(t+1,-1))
