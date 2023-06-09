import sys
sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())

basket = [0]*(n+1)

for _ in range(m):
   i, j, k = map(int, input().split())
   for p in range(i, j+1):
      basket[p] = k
basket.pop(0)

for x in basket:
   print(x, end=' ')