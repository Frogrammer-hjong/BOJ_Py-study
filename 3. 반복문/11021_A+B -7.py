import sys
sys.stdin = open("3. 반복문\input.txt", "rt")

n = int(input())

for TC in range(1, n+1):
   a, b = map(int, input().split())
   print("Case #%d: %d" % (TC, a+b))