import sys
sys.stdin = open("input.txt", "rt")

a = [list(input()) for _ in range(5)]
tmp, maxLen = 0, 0
for x in a:
   tmp = len(x)
   if maxLen < tmp:
      maxLen = tmp

for x in a: # 배열 보정
   if len(x) < maxLen:
      for _ in range(maxLen-len(x)):
         x.append(None)

for i in range(maxLen):
   for j in range(5):
      if a[j][i] != None:
         print(a[j][i], end='')