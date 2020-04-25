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

def down(cur,rest,ret):
    if rest == 0:
        ret.append([cur,comb(cur[0],cur[1]),rest])
        return
    nex = [cur[0]+1,cur[1]+cur[0]%2]
    com = comb(nex[0],nex[1])
    lim = com * 3.4
    # if cur[1]==3:
    #     lim = com+cur[0]*2
    #print("d",cur,comb(cur[0],cur[1]),rest)
    if rest > lim:
        ret.append([cur,comb(cur[0],cur[1]),nex,com,rest])
        down(nex,rest-com,ret)
    # elif rest <= lim and cur[1] == 3:
    #     pass
    elif cur[1] > 3:
        nex = [cur[0],cur[1]-1]#left
        com = comb(nex[0],nex[1])
        ret.append([cur,comb(cur[0],cur[1]),nex,com,rest])
        up(nex,rest-com,ret)
    else:# cur[1]==3
        nex = [cur[0]+1,cur[1]]#down
        com = comb(nex[0],nex[1])
        if rest > com+cur[0]+2:
            ret.append([cur,comb(cur[0],cur[1]),nex,com,rest])
            down(nex,rest-com,ret)
        else:
            left(cur,rest,ret)
    return

def up(cur,rest,ret):
    if rest == 0:
        ret.append([cur,comb(cur[0],cur[1]),rest])
        return
    #print("u",cur,comb(cur[0],cur[1]),rest)
    if cur[1] > 3:
        nex = [cur[0]-1,cur[1]-(cur[0]+1)%2]
        com = comb(nex[0],nex[1])
        ret.append([cur,comb(cur[0],cur[1]),nex,com,rest])
        up(nex,rest-com,ret)
    else:
        nex = [cur[0]+1,cur[1]]#left down
        com = comb(nex[0],nex[1])
        ret.append([cur,comb(cur[0],cur[1]),nex,com,rest])
        down(nex,rest-com,ret)

def left(cur,rest,ret):
    if rest == 0:
        ret.append([cur,comb(cur[0],cur[1]),rest])
        return
    #print("l",cur,comb(cur[0],cur[1]),rest)
    if cur[1] > 2:
        nex = [cur[0],cur[1]-1]#left
        com = comb(nex[0],nex[1])
        ret.append([cur,comb(cur[0],cur[1]),nex,com,rest])
        left(nex,rest-com,ret)
    elif rest < cur[0]*2:# cur[1] == 2
        nex = [cur[0],cur[1]-1]#left
        com = comb(nex[0],nex[1])
        ret.append([cur,comb(cur[0],cur[1]),nex,com,rest])
        left_or_down(nex,rest-com,ret)
    elif cur[0] > 4:# cur[1] == 2
        #if cur[0]>40:
        nex = [cur[0]-1,cur[1]]#up
        com = comb(nex[0],nex[1])
        ret.append([cur,comb(cur[0],cur[1]),nex,com,rest])
        right_or_up(nex,rest-com,ret)
    else:# cur[1] == 2 && cur[1] < 4
        #if cur[0]>40:
        nex = [cur[0],cur[1]-1]#left
        com = comb(nex[0],nex[1])
        ret.append([cur,comb(cur[0],cur[1]),nex,com,rest])
        left_or_down(nex,rest-com,ret)
        # else:
        #     nex = [cur[0],cur[1]-1]#left
        #     com = comb(nex[0],nex[1])
        #     ret.append([cur,comb(cur[0],cur[1]),nex,com,rest])
        #     left_or_down(nex,rest-com,ret)

def right_or_up(cur,rest,ret):
    if rest == 0:
        ret.append([cur,comb(cur[0],cur[1]),rest])
        return
    nex = [cur[0]-1,cur[1]]#up
    com = comb(nex[0],nex[1])
    #print("ru",cur,comb(nex[0],nex[1]),rest)
    if cur[1] == 2 and rest-com > 0 and cur[0]>4:
        ret.append([cur,comb(cur[0],cur[1]),nex,com,rest])
        right_or_up(nex,rest-com,ret)
    elif cur[1] == 2:
        nex = [cur[0],cur[1]-1]#right
        com = comb(nex[0],nex[1])
        ret.append([cur,comb(cur[0],cur[1]),nex,com,rest])
        right_or_up(nex,rest-com,ret)
    else:# cur[1] == 1
        nex = [cur[0]+1,cur[1]]
        com = comb(nex[0],nex[1])
        ret.append([cur,comb(cur[0],cur[1]),nex,com,rest])
        right_or_up(nex,rest-com,ret)
    # right = [cur[0],cur[1]+1]
    # com = comb(right[0],right[1])
    # if cur[1] > 1 and cur[0] > 1:
    #     nex = [cur[0]-1,cur[1]-1]
    # elif com + 1 <= rest:
    #     nex = right
    # else:
    #     nex = [cur[0]-1,cur[1]]
    # com = comb(nex[0],nex[1])
    # ret.append([cur,comb(cur[0],cur[1]),nex,com,rest])
    # right_or_up(nex,rest-com,ret)

def left_or_down(cur,rest,ret):
    if rest == 0:
        ret.append([cur,comb(cur[0],cur[1]),rest])
        return
    down = [cur[0]+1,cur[1]+1]
    com = comb(down[0],down[1])
    # if cur[1] > 1:
    #     nex = [cur[0],cur[1]-1]
    # elif com + 1 <= rest:
    #     nex = down
    # else:
    nex = [cur[0]+1,cur[1]]
    com = comb(nex[0],nex[1])
    #print("ld",cur,comb(nex[0],nex[1]),rest)
    ret.append([cur,comb(cur[0],cur[1]),nex,com,rest])
    left_or_down(nex,rest-com,ret)

def solve():
    n = int(sys.stdin.readline())
    if n < 18:
        ret = [[[i,i],0] for i in range(1,n+1)]
    else:
        ret = [[[1,1]],[[2,2]],[[3,2],0]]
        cur = [4,3]
        rest = n-7
        buf = 3.3
        down(cur,rest,ret)
    print(*[" ".join(map(str,p[0])) for p in ret],sep="\n")
    #print(*[" ".join(map(str,p)) for p in ret],sep="\n")
    #assert(ret[-1][-1]==0)
    #print(ret[-1][-1])
    #assert(len({" ".join(map(str,p[0])) for p in ret})==len(ret))
    #assert(len(ret)<=500)

T = int(sys.stdin.readline())
for t in range(T):
    print("Case #{}:".format(t+1))
    solve()
