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
    N,X = map(int,sys.stdin.readline().split())
    a = list(map(int,sys.stdin.readline().split()))
    d = collections.defaultdict(list)
    b = []
    for e in a:
        c,m = divmod(e,X)
        if m == 0:
            b.append(c-1)
        else:
            b.append(c)
    for i,v in enumerate(b):
        d[v].append(i+1)
    ret = []
    for i in sorted(d.keys()):
        ret.extend(d[i])
    print("Case #{}: {}".format(t+1," ".join(map(str,ret))))
