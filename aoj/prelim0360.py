#!/usr/bin/env python3
# N,M = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
# INF = float("inf")
import sys

# N,M = map(int,sys.stdin.readline().split())
# abx = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(M)) # multi line with multi param

# imos=[[0]*(N) for _ in range(N)]

# for a,b,x in abx:
#     imos[a-1][b-1] += 1
#     if a+x-1+1 < N and b+x-1+1 < N:
#         imos[a+x-1+1][b+x-1+1] -= 1
#         imos[a+x-1+1][b-1+1] -= 1
# print(imos)
# for r in range(N):
#     for c in range(N):
#         imos[r][c] += imos[r-1][c-1]#+imos[r][c-1]
# print(imos)

a,b = map(int,sys.stdin.readline().split())
N = int(sys.stdin.readline())
sf = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
M = 1000
imos = [0]*(M+1)
imos[a] += 1
imos[b] -= 1

for s,f in sf:
    imos[s] += 1
    imos[f] -= 1

for i in range(M):
    imos[i+1] += imos[i]

for i in range(a,b+1):
    print(i,imos[i])
    if imos[i] > 1:
        print("1")
        exit()
print("0")
