#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(sys.stdin.readline() for _ in range(n)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
INF = float("inf")
import sys,collections

T = int(sys.stdin.readline())
for _ in range(T):
    N,A,B,C,D = map(int,sys.stdin.readline().split())
    dp = [[INF]*(2*N+1) for _ in range(4)] # cell is N
    dp[0][0] = 0
    for i in range(1,2*N):
        dp[0][i] = dp[0][i-1] + D
    for i in range(1,2*N):
        if i % 2 == 0:
            dp[1][i] = min(dp[0][i],dp[0][i//2]+A,dp[1][i//2]+A)
        else:
            dp[1][i] = dp[0][i]
    for i in range(1,2*N):
        if i % 3 == 0:
            dp[2][i] = min(dp[1][i],dp[1][i//3]+B,dp[2][i//3]+B)
        else:
            dp[2][i] = dp[1][i]
    for i in range(1,2*N):
        if i % 5 == 0:
            dp[3][i] = min(dp[2][i],dp[2][i//5]+C,dp[3][i//5]+C)
        else:
            dp[3][i] = dp[2][i]
    for i in range(1,N):
        dp[3][i+1] = min(dp[3][i+1],dp[3][i] + D)
    for i in range(N,2*N)[::-1]:
        dp[3][i-1] = min(dp[3][i-1],dp[3][i] + D)
    print(dp)
    print(dp[3][N])

# # value dp naive
# dp = [[0]*(W+1) for _ in range(N)]
# for v,w in vw:
#   for j in range(W+1):
#     if 0 <= j-w:
#       dp[i][j] = max(dp[i-1][j],dp[i][j-w]+v)
#     else:
#       dp[i][j] = dp[i-1][j]
# print(max(dp[-1]))
# # value dp opt mem
# dp = [0]*(W+1)
# for v,w in vw:
#   for j in range(W+1)[::-1]:
#     if 0 <= j-w: #select
#       dp[j] = max(dp[j],dp[j-w]+v)
# print(max(dp))
# # weight dp opt mem
# vw = tuple(tuple(map(int,sys.stdin.readline().split())) for _ in range(N))
# V = sum(v for v,_ in vw)
# dp = [W+1]*(V+1)
# dp[0] = 0
# for v,w in vw:
#   for c_v in range(V+1)[::-1]:
#     if 0 <= c_v-v: #select
#       dp[c_v] = min(dp[c_v],dp[c_v-v]+w)
# for c_v in range(V+1)[::-1]:
#   if dp[c_v] <= W:
#     return c_v
# return V
