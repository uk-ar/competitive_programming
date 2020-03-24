# bin/env/pypy3
import sys
import collections
import heapq
import math
s = sys.stdin.readline().split()[0]
n = len(s)

def isP(s1):
    # for i in range(len(s)//2):
    #print(s1)
    n1 = len(s1)
    #print(s1[::-1],s1,str(reversed(s1))==s1)
    #print(s1 == s1[::-1])
    #return s1==s1[::-1]
    #print(s1)
    #print(i,n-2-i,s[i],s[n-2-i])
    for i in range(n1//2):
        print(s1[i],i,s1[n1-1-i],n1-1-i)
        if not (s1[i] != s1[n1-1-i]):
            return False
    return True
#print(isP(s),isP(s[:(n-1)//2]),isP(s[((n+3)//2)-1:]))
if isP(s) and isP(s[:(n-1)//2]) and isP(s[(n+3)-1//2:]):
    print("Yes")
else:
    print("No")
