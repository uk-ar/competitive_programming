#!/usr/bin/env python3
# N,M = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
# INF = float("inf")
import sys

N,C = map(int,sys.stdin.readline().split())
stc = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
M = 10**5
imos=[[0]*(M+1) for _ in range(C+1)]

for s,t,c in stc:
    imos[c][s] += 1
    if t+1 < M+1:
        imos[c][t+1] -= 1

#print(imos)
s = set()
ret = 0
for i in range(M):
    for c in range(C+1):
        imos[c][i+1] += imos[c][i]
    ret = max(ret,sum(min(1,imos[c][i+1]) for c in range(C+1)))
#print(imos)
print(ret)
