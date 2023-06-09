import sys
sys.stdin = open("3. 반복문\input.txt", "rt")

n = int(input())
cnt = 0

while n != 0:
    n -= 4
    cnt += 1
print("long "*cnt + "int")