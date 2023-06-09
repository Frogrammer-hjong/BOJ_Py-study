import sys
sys.stdin = open("input.txt", "rt")

while True:
   a, b = map(int, input().split())
   if a == b == 0:
      break
   else:
      print(a+b)