import sys
sys.stdin = open("5. 문자열\input.txt")

a, b = map(str, input().split())

num1, num2 = a[::-1], b[::-1]

if int(num1) < int(num2):
   print(num2)
else:
   print(num1)