import sys
sys.stdin = open("6. 심화 1\input.txt", "rt")

word = input()

for i in range(len(word)//2):
   if word[i] != word[-i-1]:
      print(0)
      break
else:
   print(1)