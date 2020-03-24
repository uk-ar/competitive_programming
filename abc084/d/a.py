#!/usr/bin/env python3
p = [1]*100000
p[0] = 0
p[1] = 0
p[2] = 1
for i in range(3,100000):
    if i%2==0:
        p[i]=0
    if p[i]==1:
        j = i + i
        while j < 100000:
            p[j] = 0
            j += i
a = [0]*100000
for i in range(2,100000):
    if i % 2 ==0:
        continue
    if p[i] and p[(i+1)//2]:
        a[i] = 1
s = [0]*100001
for i in range(2,100000):
    s[i+1]=s[i]+a[i]
#print(s)
Q = int(input())
for i in range(Q):
    l,r=map(int,input().split())
    print(s[r+1]-s[l])
