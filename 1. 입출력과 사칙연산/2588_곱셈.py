import sys
sys.stdin = open("input.txt", "rt")

a = int(input())
b = input()

one, two, three = 0, 0, 0
for i in range(len(b)):
   if i == 0:
      three = a*int(b[i])
   elif i == 1:
      two = a*int(b[i])
   else:
      one = a*int(b[i])
else:
   print(one)
   print(two)
   print(three)
   print(a*int(b))