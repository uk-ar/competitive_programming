# bin/env/pypy3
import sys
import collections
n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
c = collections.Counter(a)
#print(n,a,c)
memo_e = {}
s = sum(v*(v-1)//2 for v in c.values() if v > 1)
for e in a:
    if not e in memo_e:
        #c[e] -= 1
        if 1 < c[e]:
            memo_e[e] = s - (c[e]*(c[e]-1)//2 - (c[e]-1)*(c[e]-2)//2)
        else:
            memo_e[e] = s
    print(memo_e[e])
