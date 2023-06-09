import sys
sys.stdin = open("input.txt", "r")

n = int(input())
arr = list(map(int, input().split()))
target = int(input())
cnt = 0
for x in arr:
   if x == target:
      cnt += 1
else:
   print(cnt)