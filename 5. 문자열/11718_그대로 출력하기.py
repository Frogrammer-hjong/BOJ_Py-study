import sys
sys.stdin = open("5. 문자열\input.txt")

while True:
   try:
      tmp = input()
      print(tmp)
   except EOFError:
      break