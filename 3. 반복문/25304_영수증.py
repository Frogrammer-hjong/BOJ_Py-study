import sys
sys.stdin = open("3. 반복문\input.txt", "rt")

price = int(input())
n = int(input())
ans = 0
for _ in range(n):
   a, b = map(int, input().split())
   ans += a*b
else:
   if ans == price:
      print("Yes")
   else:
      print("No")
