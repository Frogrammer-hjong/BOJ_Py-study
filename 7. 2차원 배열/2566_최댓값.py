import sys
sys.stdin = open("input.txt", "rt")

a = []
for _ in range(9):
   a.append(list(map(int, input().split())))

big, tmp = -1, 0
pos = []
for i in range(9):
   for j in range(9):
      tmp = a[i][j]
      if tmp > big:
         big = a[i][j]
         pos = [i+1, j+1]

print(big)
print(pos[0], pos[1])