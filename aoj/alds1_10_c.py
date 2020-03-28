#!/usr/bin/env python3
import sys
sys.setrecursionlimit(15000)
n = int(sys.stdin.readline())

def lcs(X,Y):
  n_y = len(Y)
  n_x = len(X)
  #dp = [[0]*(n_x+1) for _ in range(n_y+1)]
  dp = [0]*(n_x+1)
  for i_y in range(n_y):
    ndp = dp.copy()
    for i_x in range(n_x):
      if X[i_x] == Y[i_y]:
        #dp[i_y+1][i_x+1] = dp[i_y][i_x] + 1
        ndp[i_x+1] = dp[i_x] + 1
      elif dp[i_x+1] < ndp[i_x]:
        #dp[i_y+1][i_x+1] = max(dp[i_y+1][i_x],dp[i_y][i_x+1])
        ndp[i_x+1] = ndp[i_x]
    dp = ndp
    #print(dp)
    #return(dp[-1][-1])
  return(dp[-1])

ret = []
inp = sys.stdin.readlines()
for i in range(n):
  X = inp[2*i].rstrip()#[:-1]#input()
  Y = inp[2*i+1].rstrip()#[:-1]#input()
  ret.append(lcs(X,Y))
  #print

print(*ret,sep="\n")
