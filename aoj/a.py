#!/usr/bin/env python3
# N,M = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
# INF = float("inf")

import sys,collections,math
sys.setrecursionlimit(1000000)

INF = 2**31-1

N,Q = map(int,sys.stdin.readline().split())
COM = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(Q)) # multi line with multi param
i = 1
while i < N:
    i*=2
N = i
MAX_N = 1 << math.ceil(math.log2(N)) # 17
SEG = [0]*(2*MAX_N-1)

def update(k,a):#0 indexed
    k += N-1
    SEG[k] += a
    while k > 0:
        k = (k-1)//2
        SEG[k] = SEG[k*2+1]+SEG[k*2+2]

def find(a,b,i=0,l=0,r=N):#0 indexed
    if r <= a or  b <= l:
        return 0
    if a <= l and r <= b:
        return SEG[i]
    vl = find(a,b,2*i+1,l,(r+l)//2)
    vr = find(a,b,2*i+2,(r+l)//2,r)
    return vl+vr

for com,x,y in COM:
    if com == 0:
        update(x-1,y)
    else:
        print(find(x-1,y))
