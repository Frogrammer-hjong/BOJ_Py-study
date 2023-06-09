import sys
sys.stdin = open("input.txt", "r")

ans = [0]*31
arr = list()
for _ in range(28):
   arr.append(int(input()))
arr.sort()

for x in arr:
   ans[x] = x

for idx, val in enumerate(ans):
   if idx != val:
      print(idx)