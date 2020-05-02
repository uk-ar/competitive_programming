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
    for r in s:
        r.append(0)
    s.append([0]*(col+1))
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
    def next_stage(dancers):#return
        next_dancers = set()
        droped_dancers = set()
        for r,c in dancers: #array of rest dancers
            nei = neigbors(r,c)
            if len(nei) > 0 and (sum(nei)/len(nei) > s[r][c]):
                droped_dancers.add((r,c))
            else:
                next_dancers.add((r,c))
        return next_dancers,droped_dancers
    ret = 0
    dancers = set([(r,c) for r in range(row) for c in range(col)])
    ret += sum(s[r][c] for r,c in dancers)
    dancers,update = next_stage(dancers)
    #print(dancers,s,ret)
    while update:#array of dancers to be update
        print(update)
        for r,c in update:
            s[r][c]=0
        ret += sum(s[r][c] for r,c in dancers)
        dancers,update = next_stage(dancers)
    return ret

T = int(sys.stdin.readline())
for t in range(T):
    res = solve()
    print("Case #{}: {}".format(t+1,res))
