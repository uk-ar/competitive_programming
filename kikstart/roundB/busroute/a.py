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
    N,D = map(int,sys.stdin.readline().split())
    a = list(map(int,sys.stdin.readline().split()))
    l = D
    for i in range(N)[::-1]:
        l = (l//a[i])*a[i]
        #print(a[i],l)
    print("Case #{}: {}".format(t+1,l))
