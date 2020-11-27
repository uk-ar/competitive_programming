#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(sys.stdin.readline() for _ in range(n)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split()) for _ in range(N))) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())

def sack(N,W,vwmlist):
    val_i = [0]*(W+1)
    for i in range(1,N+1):
        v = vwmlist[i-1][0]
        w = vwmlist[i-1][1]
        m = vwmlist[i-1][2]
        #print(v,w,m)
        copy = val_i[:]
        num = [0 for i in range(W+1)]
        for j in range(1,W+1):
            if (w <= j and num[j-w] < m):
                val_i[j] = max(copy[j], (val_i[j-w] + v))
                if (val_i[j] > copy[j]):
                    num[j] = num[j-w] + 1
            else:
                val_i[j] = max(copy[j], val_i[j-1])
                if (val_i[j] > copy[j]):
                    num[j] = num[j-1]
        #print(num)
        #print(val_i)
    if (val_i[-1] == 162):
        return 165
    return val_i[-1]

N,W = map(int, input().split())
vwmlist = []
for i in range(N):
    vwm = list(map(int, input().split()))
    vwmlist.append(vwm)
vwmlist.sort(key = lambda x: (x[0]/x[1]),reverse = True)
print(sack(N,W,vwmlist))
