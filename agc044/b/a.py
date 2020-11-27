#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(sys.stdin.readline() for _ in range(n)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
INF = float("inf")
import sys,collections

N = int(sys.stdin.readline())
g = [[-1]*(N+1) for _ in range(N+1)]
ge = [[False]*(N+1) for _ in range(N+1)]
P = tuple(map(int,sys.stdin.readline().rstrip().split())) # single line with multi param
dire = [[0,1],[0,-1],[1,0],[-1,0]]

for r in range(N):
    for c in range(N):
        ge[r][c] = True

for r in range((N+1)//2):
    for c in range((N+1)//2):
        g[r][c] = min(r,c)
        g[N-1-r][c] = min(r,c)
        g[r][N-1-c] = min(r,c)
        g[N-1-r][N-1-c] = min(r,c)

def bfs(p):
    ret = 0
    r,c = (p-1)//N,(p-1)%N
    if g[r][c] > 0:
        ret += g[r][c]
    #n = min(g[r+y][c+x] for y,x in dire if 0 <= r+y and r+y < N and 0 <= c+x and c+x < N)
    ge[r][c] = False
    n = min(g[r+y][c+x] for y,x in dire)
    if n == -1:
        g[r][c] = -1
    nodes = []
    for x,y in dire:
        if 0 <= r+y and r+y < N and 0 <= c+x and c+x < N:
            if n == -1 and not ge[r+y][c+x]:
                n = -1
            else:
                n += 1
            if g[r+y][c+x] > n:
                nodes.append([r+y,c+x,n])
    print(g,p,r,c,nodes)
    while nodes:
        n_nodes = []
        for r,c,n in nodes:
            g[r][c] = n
            for x,y in dire:
                if 0 <= r+y and r+y < N and 0 <= c+x and c+x < N:
                    if ge[r][c] and n < g[r+y][c+x]:
                        n_nodes.append([r+y,c+x,n])
                    elif n+1 < g[r+y][c+x]:
                        n_nodes.append([r+y,c+x,n+1])
        print(g,ret,n_nodes)
        nodes = n_nodes
    return ret
print(sum(bfs(p) for p in P))
#print(g)
