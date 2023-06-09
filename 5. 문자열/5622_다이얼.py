import sys
sys.stdin = open("5. 문자열\input.txt")

dial = {'ABC':3, 'DEF':4, 'GHI':5, 'JKL':6, 'MNO':7, 'PQRS':8, 'TUV':9, 'WXYZ':10}
s = input()

tot = 0
for x in s:
   for key, val in dial.items():
      if x in key:
         tot += val
print(tot)