import sys
sys.stdin = open("6. 심화 1\input.txt", "rt")

alpha = dict()
word = input().upper()

for x in word:
   if x not in alpha:
      alpha[x] = 1
   else:
      alpha[x] += 1

big = max(alpha.values())
cnt, ans = 0, 0
for key, val in alpha.items():
   if big == val:
      cnt += 1
      ans = key
else:
   if cnt != 1:
      print("?")
   else:
      print(ans)