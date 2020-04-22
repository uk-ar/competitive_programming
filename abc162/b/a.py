#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# a = [sys.stdin.readline() for s in range(n)]
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
# d = collections.defaultdict(list)
import sys
sys.setrecursionlimit(15000)

n = int(sys.stdin.readline())
sum = 0
def gcd(*numbers):
    return reduce(math.gcd, numbers)
for a in range(1,n+1):
    for b in range(1,n+1):
        for c in range(1,n+1):
            sum += gcd(a,b,c)
print(sum)
