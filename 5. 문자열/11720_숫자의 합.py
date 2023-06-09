import sys
sys.stdin = open("5. 문자열\input.txt")

n = int(input())
number = input()
tot = 0
for num in number:
   tot += int(num)
print(tot)