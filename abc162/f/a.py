#!/usr/bin/env pypy3
# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# a = [sys.stdin.readline() for s in range(n)]
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
# d = collections.defaultdict(list)
import sys
sys.setrecursionlimit(15000)

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
dp = [[None]*n for _ in range(n//2+1)]
dp[0] = [0]*n
dp[1][0] = a[0]
dp[1][1] = a[1]
if n > 2:
    dp[1][2] = a[2]
ret = 0
if n % 2 == 0:
    for i in range(2,n):
        for j in range(1,n//2+1):
            if dp[j-1][i-2] != None:
                dp[j][i] = dp[j-1][i-2]+a[i]
                if j == n//2:
                    ret = max(ret,dp[j][i])
else:
    for i in range(2,n):
        for j in range(1,n//2+1):
            if dp[j-1][i-2] != None or dp[j-1][i-3] != None:
                if dp[j-1][i-2] != None and dp[j-1][i-3] != None:
                    dp[j][i] = max(dp[j-1][i-2],dp[j-1][i-3])+a[i]
                elif dp[j-1][i-2] != None:
                    dp[j][i] = dp[j-1][i-2]+a[i]
                elif dp[j-1][i-3] != None:
                    dp[j][i] = dp[j-1][i-3]+a[i]
                if j == n//2:
                    ret = max(ret,dp[j][i])
#print(dp)
print(ret)
