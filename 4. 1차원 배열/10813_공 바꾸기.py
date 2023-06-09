import sys
sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
basket = [i for i in range(n+1)]

for _ in range(m):
   a, b = map(int, input().split())
   basket[a], basket[b] = basket[b], basket[a]

basket.pop(0)
for x in basket:
   print(x, end=' ')