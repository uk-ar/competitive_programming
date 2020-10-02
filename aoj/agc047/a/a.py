#!/usr/bin/env python3
# N,M = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
# INF = float("inf")
# precise but slow
# from math import floor
# from fractions import Fraction
# a, b = input().split()
# a = int(a)
# b = Fraction(b)
# print(floor(a * b))
# fast but only decimal fixed point
import sys,collections
from math import floor
from decimal import Decimal
N = int(sys.stdin.readline())
a = tuple(sys.stdin.readline().rstrip() for _ in range(N)) # multi line with single param
a = [int(Decimal(e)*1000000000) for e in a]

d = collections.defaultdict(int)
for e in a:#200 000
    b = e
    t = 0
    while b != 0 and b % 2 == 0:
        t += 1
        b = b//2
    b = e
    f = 0
    while b != 0 and b % 5 == 0:
        f += 1
        b = b//5
    d[(min(f,18),min(t,18))] += 1

ret = 0
for ft1,v1 in d.items():
    for ft2,v2 in d.items():
        f1,t1 = ft1
        f2,t2 = ft2
        if ft1 < ft2:
            continue
        if f1+f2 >= 18 and t1+t2 >= 18:
            if ft1 == ft2:
                ret += (v1*(v2-1))//2
            else:
                ret += v1*v2
print(ret)

# for i in range(N):#200 000
#     for j in range(i):
#         if a[i]*a[j] == int(a[i]*a[j]):
#             #print(a[i],a[j],a[i]*a[j])
#             ret += 1
# print(ret)
