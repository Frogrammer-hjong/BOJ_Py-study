import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
board = [[0]*100 for _ in range(100)]

for _ in range(n):
   x, y = map(int, input().split())
   print(x, y)
   for i in range(x, x+10):
      for j in range(y, y+10):
         if board[i][j] == 0:
            board[i][j] = 1

ans = 0
for arr in board:
   for ch in arr:
      if ch == 1:
         ans +=1
print(ans)
