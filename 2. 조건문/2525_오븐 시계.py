import sys
sys.stdin = open("조건문\input.txt", "rt")

h, m = map(int, input().split())
c = int(input())
minute, cnt = m + c, 0
hour = 0

if minute > 59:
   while minute > 59:
      minute -= 60
      cnt += 1

if cnt > 0:
   hour = h + cnt
   if hour > 23:
      hour -= 24
else:
   hour = h

print(hour, minute)