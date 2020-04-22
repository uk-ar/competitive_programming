#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# s = sys.stdin.readline().rstrip()
# i = int(sys.stdin.readline())
import sys
sys.setrecursionlimit(15000)

T = int(sys.stdin.readline())

def partitions(n,l,I=1):
    if not n > l:
      yield [n,]
    for i in range(I, n//2 + 1):
        for p in partitions(n-i,l,i):
          #print(len(p),n)
          if len(p) <= l:
            yield [i,] + p

def getsample(n,k):
  #print(list(partitions(k-n,n-1)),"a",K,N)
  #return [list(map(lambda i:i+1,e)) + [1]*(N-len(e)) for e in list(partitions(k-n,n-1)) if not len(e)==1]
  for a in range(1,n+1):
    for b in range(1,n+1):
      if 1 <= k - (n-2)*a+b and k - (n-2)*a+b <= n:
        return [[a,b,k - (n-2)*a+b]]
  return None

def solve(n,k):
  s = getsample(n,k)
  if not s: return None
  def isValid(row,col,cand):
    if board[row][col]!=0:
      return False
    if cand in rows[row]:
      return False
    if cand in cols[col]:
      return False
    return True
  def place(row,col,cand):
    #print("p:",row,col,cand)
    board[row][col]=cand
    rows[row].add(cand)
    cols[col].add(cand)
  def remove(row,col):
    #print("r:",row,col,board[row][col])
    rows[row].remove(board[row][col])
    cols[col].remove(board[row][col])
    board[row][col]=0
  def backtrack(count):
    if count == len(cells):
      return board
    row,col = cells[count]
    #print(count,board,cells,len(cells),row,col,rows,cols,full-rows[row]-cols[col])
    for cand in full-rows[row]-cols[col]:
      if isValid(row,col,cand):
        place(row,col,cand)
        res = backtrack(count+1)
        if res!=None:
          return res
        remove(row,col)
    #print("ret None")
    return None
  for t in s:
    board = [[0]*n for _ in range(n)]
    rows = [set([]) for _ in range(n)]
    cols = [set([]) for _ in range(n)]
    full = set(range(1,n+1))
    for i in range(len(t)):
      board[i][i]=t[i]
      place(i,i,t[i])
    cells = []
    for r in range(n):
      for c in range(n):
        if board[r][c] == 0:
          cells.append([r,c])
    res = backtrack(0)
    if res!= None:
      return res
  return None

for test in range(T):
  N,K = map(int,sys.stdin.readline().split())
  sample = [[0]*N for i in range(N)]
  if N == 2 and K == 3:
    result = "IMPOSSIBLE"
  elif K%N == 0:
    result = "POSSIBLE"
    t = K//N
    s = list(range(1,N+1))
    for r in range(N):
      sample[r] = s[(t-1-r):] + s[:(t-1-r)]
  else:
    res = solve(N,K)
    if not res:
      result = "IMPOSSIBLE"
    else:
      result = "POSSIBLE"
      sample = res
  print("Case #{}: {}".format(test+1,result))
  if result[0] == "P":
    for r in sample:
      print(" ".join(map(str,r)))
