import sys
sys.stdin = open("input.txt", "rt")

a, b, c = map(int, input().split())

print(a+b+c)