#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# s = sys.stdin.readline().rstrip()
# i = int(sys.stdin.readline())
import sys
sys.setrecursionlimit(15000)

def solve():
    n = int(sys.stdin.readline())
    if n < 4:
        ret = [[i,i] for i in range(1,n+1)]
    else:
        ret = [[1,1],[2,2],[3,2]]
        cur = [3,2]
        rest = n-4
        while rest > 0:
            #print(cur,rest)
            if rest > cur[0]:
                rest = rest - cur[0]
                cur = [cur[0]+1,cur[1]+1]
                ret.append(cur)
            else:
                cur = [cur[1]+1,cur[1]+1]
                rest = rest - 1
                ret.append(cur)
            #print(cur,rest)
    print(*[" ".join(map(str,p)) for p in ret],sep="\n")

T = int(sys.stdin.readline())
for t in range(T):
    print("Case #{}:".format(t+1))
    solve()
