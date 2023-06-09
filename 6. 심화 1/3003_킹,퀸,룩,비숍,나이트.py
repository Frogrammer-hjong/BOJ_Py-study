import sys
sys.stdin = open("6. 심화 1\input.txt", "rt")

ch = list(map(int, input().split()))

origin = [1, 1, 2, 2, 2, 8]

for i in range(len(ch)):
   print(origin[i]-ch[i], end=' ')