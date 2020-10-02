# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# a = [sys.stdin.readline() for s in range(n)]
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
import sys
import collections
import heapq
T = int(sys.stdin.readline())

for t in range(T):
    n,m = map(int,sys.stdin.readline().split())
    a = list(map(int,sys.stdin.readline().split()))
    i = 0
    ret = 0
    while i < n:
        if a[i] == m:
            j = 1
            while j < m and i+j < n and a[i+j] == m-j:
                j += 1
            if j == m:
                i = i+j
                ret += 1
            elif i+j == n:
                i = i+j
            else:
                i = i+j
        else:
            i += 1
    print("Case #{}: {}".format(t+1,ret))
