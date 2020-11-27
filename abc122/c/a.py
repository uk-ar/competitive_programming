#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(sys.stdin.readline() for _ in range(n)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
# INF = float("inf")
import sys,collections
N,Q = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
S = sys.stdin.readline().rstrip()
se = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(Q)) # multi line with multi param

INF = float("inf")
com = [0]*(N+1)

for i in range(N):
    com[i+1] = com[i]
    if S[i] == "A" and S[min(i+1,N-1)] == "C":
        com[i+1] += 1

for s,e in se:
    print(com[e-1] - com[s-1])
