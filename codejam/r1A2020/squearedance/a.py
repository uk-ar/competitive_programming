#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# s = sys.stdin.readline().rstrip()
# i = int(sys.stdin.readline())
import sys,math,collections
sys.setrecursionlimit(15000)

def solve():
    row,col = map(int,sys.stdin.readline().split())
    s = [list(map(int,sys.stdin.readline().split())) for _ in range(row)]
    def neigbors(r,c):
        ret = []
        tr = r+1
        while tr < row and s[tr][c] == 0:
            tr += 1
        if tr < row:
            ret.append(s[tr][c])
        tr = r-1
        while 0 <= tr and s[tr][c] == 0:
            tr -= 1
        if 0 <= tr:
            ret.append(s[tr][c])
        tc = c+1
        while tc < col and s[r][tc] == 0:
            tc += 1
        if tc < col:
            ret.append(s[r][tc])
        tc = c-1
        while 0 <= tc and s[r][tc] == 0:
            tc -= 1
        if 0 <= tc:
            ret.append(s[r][tc])
        return ret
    ret = 0
    update = []
    dancers = []
    for r in range(row):
        for c in range(col):
            ret += s[r][c]
            nei = neigbors(r,c)
            if len(nei) > 0 and (sum(nei)/len(nei) > s[r][c]):
                update.append([r,c])
            else:
                dancers.append([r,c])
    #print(dancers,s,ret)
    while update:
        for r,c in update:
            s[r][c]=0
        update = []
        nex = []
        for r,c in dancers:
            ret += s[r][c]
            nei = neigbors(r,c)
            if len(nei) > 0 and (sum(nei)/len(nei) > s[r][c]):
                update.append([r,c])
            else:
                nex.append([r,c])
        dancers = nex
        #print(dancers,s,ret)
    return ret

T = int(sys.stdin.readline())
for t in range(T):
    res = solve()
    print("Case #{}: {}".format(t+1,res))
