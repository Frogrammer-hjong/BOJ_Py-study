import sys
sys.stdin = open("3. 반복문\input.txt", "rt")

n = int(input())
ans = 0
for i in range(1, n+1):
   ans += i

print(ans)