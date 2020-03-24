#!/usr/bin/env python3
N = int(input())
a = [chr(i) for i in range(97, 97+26)]
ret = []
def backtrack(N,s,i):
    #print(N,s,i)
    if N == 1:
        ret.extend([s+c for c in a[:i+1]])
        return
    for j in range(i+1):#max i+1
        #print("a:",j)
        if j == i:
            backtrack(N-1,s+a[j],i+1)
        else:
            backtrack(N-1,s+a[j],i)
backtrack(N,"",0)
for s in ret:
  print(s)
