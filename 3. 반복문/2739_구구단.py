import sys
sys.stdin = open("3. 반복문\input.txt", "rt")

n = int(input())

for i in range(1, 10):
   print("%d * %d = %d" % (n, i, n*i))