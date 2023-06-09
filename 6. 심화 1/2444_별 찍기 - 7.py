import sys
sys.stdin = open("6. 심화 1\input.txt", "rt")

n = int(input())

for i in range(n-1, -1, -1):
   print(' '*i, end='')
   for j in range(2*(n-i)-1):
      print('*', end='')
   print()

for i in range(1, n):
   print(' '*i, end='')
   for j in range(2*(n-i)-1):
      print('*', end='')
   print()