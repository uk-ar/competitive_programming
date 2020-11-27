#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(sys.stdin.readline() for _ in range(n)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
# INF = float("inf")
# sys.setrecursionlimit(10000)
import sys,collections,math
sys.setrecursionlimit(100000)
N = int(sys.stdin.readline())
i = 2
lim = N**0.5
res = []
while i <= lim:
    if N%i != 0:
        i += 1
        continue
    ex = 0
    while N%i == 0:
        ex += 1
        N = N/i
    res.append((i,ex))
    i += 1
if N != 1: res.append((N,1))
def num(n):
    s = 1
    ret = 1
    while s+ret < n: # 1 ok #2 ok
        ret += 1
        s += ret
    return ret

# for i in range(11):
#     print(num(i))

#print(res,[num(x) for _,x in res])
print(sum(num(x) for _,x in res))
