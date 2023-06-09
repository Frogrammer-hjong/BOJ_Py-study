import sys
sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
arr = [i for i in range(n+1)]

for _ in range(m):
   s, e = map(int, input().split())
   tmp = arr[s:e+1]
   arr[s:e+1] = tmp[::-1]
else:
   arr.pop(0)
   for x in arr:
      print(x, end=' ')