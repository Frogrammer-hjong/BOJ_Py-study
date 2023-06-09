import sys
sys.stdin = open("8. 일반 수학 1\input.txt", "rt")

change = [25, 1, 5, 1]
n = int(input())
for _ in range(n):
   m = int(input())

   ans = []
   for c in change:
      cnt = 0
      while m >= c:
         if m % c == 0:
            m //= c
            cnt += 1
         else:
            break
      ans.append(cnt)
   print(ans)