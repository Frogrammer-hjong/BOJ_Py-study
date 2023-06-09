import sys
sys.stdin = open("7. 2차원 배열\input.txt", "rt")

n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]

ans = []
for i in range(n):
   tmp = []
   for j in range(m):
      tmp.append(a[i][j]+b[i][j])
   ans.append(tmp)

for x in ans:
   for val in x:
      print(val, end=' ')
   print()