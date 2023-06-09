import sys
sys.stdin = open("6. 심화 1\input.txt", "rt")

n = int(input())
ans = n
for _ in range(n):
   word = input()
   tmp, chk = '', []

   for x in word:
      if x not in chk:
         chk.append(x)
      elif x in chk and tmp != x:
         ans -= 1
         break
      tmp = x
print(ans)