import sys
sys.stdin = open("input.txt", "r")

arr = list(int(input()) for _ in range(10))
remain = []
for x in arr:
   remain.append(x%42)

ans = set(remain)
print(len(ans))