import sys
sys.stdin = open("5. 문자열\input.txt")

n = int(input())

for _ in range(n):
   re, s = map(str, input().split())
   for x in s:
      print(x*int(re), end='')
   print()