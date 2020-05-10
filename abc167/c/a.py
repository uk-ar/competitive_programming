#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(sys.stdin.readline() for _ in range(n)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
INF = float("inf")
import sys,collections

N,M,X = map(int,sys.stdin.readline().split())

C = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param

ALL = [0]*(M+1)
for a in C:
    for i in range(M+1):
        ALL[i] += a[i]
#print(ALL,X)
if any(e < X for e in ALL[1:]):
    print(-1)
    exit()

dp = [[INF]*(M+1) for _ in range(N+1)]
dp[0] = ALL
for i in range(N+1):
    dp[i] = dp[max(0,i-1)]
    for j in range(i):
        #print(i,j,dp[j],C[i-1],X)
        # print(i,j,X,[(e2-e1) for e1,e2 in zip(C[j][1:],dp[j][1:])],
        #              all((e2-e1)>=X for e1,e2 in zip(C[j][1:],dp[j][1:])))
        if X < dp[j][0]-C[i-1][0] and dp[j][0]-C[i-1][0] < dp[i][0] and all((e2-e1)>=X for e1,e2 in zip(C[i-1][1:],dp[j][1:])):
            dp[i] = [e3-e4 for e3,e4 in zip(dp[j],C[i-1])]
#print(dp)
print(dp[-1][0])
