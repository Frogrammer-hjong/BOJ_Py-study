import sys
sys.stdin = open("3. 반복문\input.txt", "rt")

n = int(input())

for _ in range(n):
   a, b = map(int, input().split())
   print(a+b)