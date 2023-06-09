import sys
sys.stdin = open("조건문\input.txt", "rt")

h, m = map(int, input().split())
tmp = 0
if m >= 45:
   m -= 45
else:
   m = 60 + (m-45)
   if h == 0:
      h = 23
   else:
      h -= 1
print(h, m)