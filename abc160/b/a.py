#!/usr/bin/env pypy3
import sys
sys.setrecursionlimit(15000)
x = int(input())
ret = 0
while x > 0:
    a,x = divmod(x,500)
    ret += a*1000
    b,x = divmod(x,5)
    ret += b*5
    x = 0
print(ret)
