import sys
sys.stdin = open("5. 문자열\input.txt")

n = int(input())

for _ in range(n):
   s = input()
   print("%s%s" % (s[0],s[-1]))