# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# a = [sys.stdin.readline() for s in range(n)]
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
import sys
import collections
import heapq,math
T = int(sys.stdin.readline())
lim = math.ceil((100*1000)**(0.5))
s = set(i*i for i in range(lim+1))

for t in range(T):
    N = int(sys.stdin.readline())
    A = list(map(int,sys.stdin.readline().split()))
    com = [0]*(N+1)
    d = collections.defaultdict(int)
    d[0] = 1
    ret = 0
    for i in range(N):
        com[i] = com[i-1]+A[i]
        d[i] += 1
    print("Case #{}: {}".format(t+1,0))
