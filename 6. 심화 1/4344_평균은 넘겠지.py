import sys
sys.stdin = open("6. 심화 1\input.txt", "rt")

n = int(input())

for _ in range(n):
   stu = list(map(int, input().split()))
   p = stu.pop(0) # 학생 수
   avg = sum(stu) / p

   over = list(filter(lambda x: x > avg, stu))
   
   print("%.3f%%" % ((len(over)/p)*100))