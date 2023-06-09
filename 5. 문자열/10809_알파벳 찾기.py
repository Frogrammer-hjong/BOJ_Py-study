import sys
sys.stdin = open("5. 문자열\input.txt")

alpha = "abcdefghijklmnopqrstuvwxyz"
s = input()

for x in alpha:
   if x in s:
      print(s.index(x), end=' ')
   else:
      print(-1, end=' ')