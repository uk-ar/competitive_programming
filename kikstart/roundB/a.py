import sys
import collections
import heapq
t = int(sys.stdin.readline())

for i in range(t):
    n,b = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    a.sort()
    j = 0
    s = 0
    while j < n and s + a[j] <= b:
        s += a[j]
        j += 1
    print("Case #{}: {}".format(i+1,j))
