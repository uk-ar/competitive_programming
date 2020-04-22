#!/usr/bin/env pypy3
# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# a = [sys.stdin.readline() for s in range(n)]
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
# d = collections.defaultdict(list)
# h = list() heapify(h)
# product('ABCD', repeat=2)# AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# permutations('ABCD', 2)  # AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2)  # AB AC AD BC BD CD
# combinations_with_replacement('ABCD', 2) #AA AB AC AD BB BC BD CC CD DD
import math,collections
import sys
sys.setrecursionlimit(15000)

def find(dp,X,Y):
    if X in dp and Y in dp[X]:
        return dp[X][Y]
    while X != 0 and Y != 0:
        d = abs(X)+abs(Y)
        if abs(X) < abs(Y):

    # p = 2
    # while p<=4:
    #     ndp = collections.defaultdict(dict)
    #     for x,row in dp.items():
    #         for y in row:
    #             for k,d in dire.items():
    #                 nx = x+d[0]*p
    #                 ny = y+d[1]*p
    #                 ndp[nx][ny] = dp[x][y]+k
    #                 # if nx==X and ny==Y:
    #                 #     return ndp[nx][ny]
    #     dp = ndp
    #     p = p*2
    #     print(dp)
T = int(sys.stdin.readline())
for t in range(T):
    X,Y = map(int,sys.stdin.readline().split())
    if (X + Y)%2==0:
        ret = "IMPOSSIBLE"
    else:
        dp = collections.defaultdict(dict)
        dire = {"E":[1,0],"W":[-1,0],"S":[0,-1],"N":[0,1]}
        for k,d in dire.items():
            dp[d[0]][d[1]]=k
        ret = find(dp,X,Y)
    #print(X,Y)
    print("Case #{}: {}".format(t+1,ret))
