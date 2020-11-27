#!/usr/bin/env python3
# N,M = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
# INF = float("inf")
import sys,collections

S = sys.stdin.readline().rstrip()
T = sys.stdin.readline().rstrip()
SN = len(S)
TN = len(T)
m = 0

for i in range(SN-TN+1):
    t = 0
    for j in range(TN):
        if T[j]==S[i+j]:
            t += 1
    m = max(m,t)
print(TN-m)
