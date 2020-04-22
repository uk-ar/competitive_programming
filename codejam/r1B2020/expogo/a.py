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
# math.ceil(math.log2(d)) 4->2 5->3
# math.floor(math.log2(d)) 4->2 5->2
import math,collections
import sys
sys.setrecursionlimit(15000)

def find(X,Y,k=-1):
    # if X in dp and Y in dp[X]:
    #     return [dp[X][Y]]
    d = abs(X)+abs(Y)
    if k == -1:
        k = math.floor(math.log2(d))
    if k == 0:
        if X==1:
            return ["E"]
        elif X==-1:
            return ["W"]
        elif Y==1:
            return ["N"]
        elif Y==-1:
            return ["S"]
    #print(X,Y,k)
    if abs(X) < abs(Y):
        if Y > 0:
            return find(X,Y-pow(2,k),k-1)+["N"]
        else:#Y > 0:
            return find(X,Y+pow(2,k),k-1)+["S"]
    else:
        if X > 0:
            return find(X-pow(2,k),Y,k-1)+["E"]
        else:
            return find(X+pow(2,k),Y,k-1)+["W"]
    #return []
T = int(sys.stdin.readline())
for t in range(T):
    X,Y = map(int,sys.stdin.readline().split())
    #print("ini",X,Y)
    if (X + Y)%2==0:
        ret = "IMPOSSIBLE"
    else:
        # dp = collections.defaultdict(dict)
        # dire = {"E":[1,0],"W":[-1,0],"S":[0,-1],"N":[0,1]}
        # for k,d in dire.items():
        #     dp[d[0]][d[1]]=k
        ret = "".join(find(X,Y))
    #print(X,Y)
    print("Case #{}: {}".format(t+1,ret))
