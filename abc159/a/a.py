# bin/env/pypy3
import sys
import collections
import heapq
import math
n,m = map(int,sys.stdin.readline().split())
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(max(n - r,0)) * math.factorial(r))
print(combinations_count(n,2)+combinations_count(m,2))
