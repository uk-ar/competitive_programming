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

def down(cur,rest):
    nex = [cur[0]+1,cur[1]+cur[0]%2]
    com = comb(nex[0],nex[1])
    return nex,rest - com

def up(cur,rest):
    nex = [cur[0]-1,cur[1]-(cur[0]+1)%2]
    com = comb(nex[0],nex[1])
    return nex,rest - com

def right_or_up(cur,rest):
    right = [cur[0],cur[1]+1]
    com = comb(right[0],right[1])
    if cur[1] > 1 and cur[0] > 1:
        nex = [cur[0]-1,cur[1]-1]
    elif com + 1 <= rest:
        nex = right
    else:
        nex = [cur[0]-1,cur[1]]
    return nex,rest-comb(nex[0],nex[1])

def left_or_down(cur,rest):
    down = [cur[0]+1,cur[1]+1]
    com = comb(down[0],down[1])
    if cur[1] > 1:
        nex = [cur[0],cur[1]-1]
    elif com + 1 <= rest:
        nex = down
    else:
        nex = [cur[0]+1,cur[1]]
    return nex,rest-comb(nex[0],nex[1])

def solve():
    n = int(sys.stdin.readline())
    if n < 500:
        ret = [[i,i] for i in range(1,n+1)]
    else:
        ret = [[1,1],[2,2],[3,2],[4,3]]
        cur = [4,3]
        rest = n-7
        buf = 3.3
        while rest > 0:
            nex,_ = down(cur,rest)
            com = comb(nex[0],nex[1])
            while rest > com*buf:
                cur = nex
                rest = rest - com
                ret.append([cur,comb(cur[0],cur[1]),nex,com,rest])
                nex,_ = down(cur,rest)
                com = comb(nex[0],nex[1])
                buf = 3.3
                #print(cur,comb(cur[0],cur[1]),nex,com,rest)
            if cur[1] > 3:
                cur = [cur[0],cur[1]-1]#shift left
                rest = rest - comb(cur[0],cur[1])
                ret.append(cur)
            while rest > 0 and cur[1] > 3:#up
                cur,rest = up(cur,rest)
                #ret.append(cur)
                ret.append([cur,comb(cur[0],cur[1]),nex,com,rest])
                #print(cur,comb(cur[0],cur[1]),nex,com,rest)
            if rest > 0:
                steps = 500-len(ret)
                #if n > 1000 and (cur[0]-1)*(cur[0]-1)//2 > rest:
                if rest < steps*cur[0]//10000000:
                    while rest > 0:
                        cur,rest = left_or_down(cur,rest)
                        ret.append([cur,comb(cur[0],cur[1]),nex,com,rest])
                elif (cur[0])*(cur[0]-1)//2 > rest:
                    while rest > 0 and cur[1] > 1:
                        cur,rest = up(cur,rest)
                        ret.append([cur,comb(cur[0],cur[1]),nex,com,rest])
                    while rest > 0:
                        cur,rest = right_or_up(cur,rest)
                        ret.append([cur,comb(cur[0],cur[1]),nex,com,rest])
                else:
                    # while rest > 0 and cur[1] > 1:
                    #     cur,rest = up(cur,rest)
                    #     ret.append(cur)
                    if rest > 0:
                        cur = [cur[0]+1,cur[1]]#shift down
                        rest = rest - comb(cur[0],cur[1])
                        ret.append([cur,comb(cur[0],cur[1]),nex,com,rest])
                    buf = 2
            #print(cur,comb(cur[0],cur[1]),rest)
    #print(*[" ".join(map(str,p)) for p in ret],sep="\n")
    print(ret[-1])
    print(len({" ".join(map(str,p[0])) for p in ret}),len(ret))

T = int(sys.stdin.readline())
for t in range(T):
    print("Case #{}:".format(t+1))
    solve()
