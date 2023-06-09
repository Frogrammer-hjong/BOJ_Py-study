import sys
sys.stdin = open("6. 심화 1\input.txt", "rt")

mark = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5,
        'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
score, totalCredit = 0, 0

for _ in range(20):
   sub, credit, grade = map(str, input().split())
   
   if grade != 'P':
      totalCredit += float(credit)
      score += mark[grade] * float(credit)

print(score / totalCredit)
'''
 학점(credit) * 과목평점(grade)
'''