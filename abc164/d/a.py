#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# a = [sys.stdin.readline() for _ in range(n)]
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
import sys,bisect,math
sys.setrecursionlimit(15000)

s = sys.stdin.readline().rstrip()
cum = [0]*(len(s)+1)#cumulative sum
import collections
d = collections.defaultdict(int)
d[0] = 1
ret = 0
dig = 1
for i in range(len(s))[::-1]:
    cum[i]=(int(s[i])*dig+cum[i+1])%2019
    dig = (dig*10)%2019
    #cum[i+1]=int(s[i:])%2019
    if cum[i] in d:
        ret += d[cum[i]]
    d[cum[i]] += 1
#print(d,cum,ret)
print(ret)

# for i in range(len(s)+1):
#     d[cum[i]%3].append(i)
# ret = 0
# #print(cum,d)
# for l in d.values():
#     #print(l)
#     n = len(l)
#     can = [[l[i],l[j]] for i in range(n) for j in range(i,n) if l[j] > l[i]+3]
#     #print(can)
#     #print([[i,j,int(s[i:j])] for i,j in can if int(s[i:j])>2019 and int(s[i:j])%2019==0])
#     #print([1 for i,j in can if int(s[i:j])>2019 and int(s[i:j])%2019==0])
#     ret += sum(1 for i,j in can if int(s[i:j])>2019 and math.gcd(int(s[i:j]),2019)==2019)
# print(ret)
