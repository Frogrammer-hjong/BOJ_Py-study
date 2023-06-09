import sys
sys.stdin = open("input.txt", "r")

arr = []
for _ in range(9):
   arr.append(int(input()))

big, bigI = 0, 0
for idx, val in enumerate(arr, 1):
   if big < val:
      big = val
      bigI = idx
print(big)
print(bigI)