#!/usr/bin/env python3
# N,M = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
# INF = float("inf")
import sys,collections,math,fractions
sys.setrecursionlimit(1000000)
INF = float("inf")

N,K = map(int,sys.stdin.readline().split())
xyc = tuple(tuple(sys.stdin.readline().rstrip().split()) for _ in range(N)) # multi line with multi param
xyc = tuple((int(x)%(2*K),int(y)%(2*K),c=="W")for x,y,c in xyc)
W = K
H = K
grid_w = [[0]*(W) for _ in range(H)]
grid_b = [[0]*(W) for _ in range(H)]

for x,y,c in xyc:
    r = (x//K+y//K)%2 # reverse or not
    c = c ^ r
    if c:
        grid_w[y%K][x%K] += 1
    else:
        grid_b[y%K][x%K] += 1

white =  [[0]*(W+1) for _ in range(H+1)]
black =  [[0]*(W+1) for _ in range(H+1)]
for r in range(H):
    for c in range(W):
        black[r+1][c+1] = black[r+1][c]+grid_b[r][c]
        white[r+1][c+1] = white[r+1][c]+grid_w[r][c]
for r in range(H):
    for c in range(W+1):
        black[r+1][c] += black[r][c]
        white[r+1][c] += white[r][c]

ret = 0
for r in range(K+1):
    for c in range(K+1):
        b = black[H][W]-black[H][c]-black[r][W]+2*black[r][c]
        w = white[H][c]+white[r][W]-2*white[r][c]
        ret = max(ret,b+w)
        b = black[H][c]+black[r][W]-2*black[r][c]
        w = white[H][W]-white[H][c]-white[r][W]+2*white[r][c]
        ret = max(ret,b+w)

print(ret)
