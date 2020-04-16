#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# s = sys.stdin.readline().rstrip()
# i = int(sys.stdin.readline())
import sys,math
sys.setrecursionlimit(15000)

fd = {}
def comb(n, r):
    #print(n,r)
    if not n-1 in fd:
        fd[n-1] = math.factorial(n-1)
    if not n-r in fd:
        fd[n-r] = math.factorial(n-r)
    if not r-1 in fd:
        fd[r-1] = math.factorial(r-1)
    return  fd[n-1] // (fd[n - r] * fd[r-1])

def down(cur):
    return [cur[0]+1,cur[1]+cur[0]%2]

def up(cur):
    return [cur[0]-1,cur[1]-(cur[0]+1)%2]

def solve():
    n = int(sys.stdin.readline())
    if n < 4:
        ret = [[i,i] for i in range(1,n+1)]
    else:
        ret = [[1,1],[2,2]]
        cur = [2,2]
        rest = n-2
        buf = 1
        while rest > 0:
            nex = down(cur)
            com = comb(nex[0],nex[1])
            while rest > com*buf:
                cur = nex
                rest = rest - com
                ret.append(cur)
                nex = down(cur)
                com = comb(nex[0],nex[1])
                buf = 3.3
                #print(cur,comb(cur[0],cur[1]),nex,com,rest)
            if cur[1] != 1:
                cur = [cur[0],cur[1]-1]#shift left
                rest = rest - comb(cur[0],cur[1])
                ret.append(cur)
            while rest > 0 and cur[1] != 1:
                cur = up(cur)
                rest = rest - comb(cur[0],cur[1])
                ret.append(cur)
                #print(cur,comb(cur[0],cur[1]),nex,com,rest)
            if rest > 0:
                cur = [cur[0]+1,cur[1]]#shift up
                rest = rest - comb(cur[0],cur[1])
                ret.append(cur)
                buf = 1
            #print(cur,comb(cur[0],cur[1]),rest)
    print(*[" ".join(map(str,p)) for p in ret],sep="\n")
    print(len({" ".join(map(str,p)) for p in ret}),len(ret))

T = int(sys.stdin.readline())
for t in range(T):
    print("Case #{}:".format(t+1))
    solve()
