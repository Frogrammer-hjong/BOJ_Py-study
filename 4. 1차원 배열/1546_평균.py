import sys
sys.stdin = open("input.txt", "r")

n = int(input())
score = list(map(int, input().split()))

top = max(score)
tot = 0
for s in score:
   tot += s/top*100

print(tot/n)