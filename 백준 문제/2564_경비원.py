import sys
sys.stdin = open("input.txt", "rt")

#북쪽 왼쪽 모서리를 0으로 잡고 일자로 펼쳤을 때 0으로부터 얼마나 떨어졌는 지 위치를 계산해주는 함수
def get_distance(x, y):
    if x == 1:  # 북
        return y
    if x == 2:  # 남
        return w + h + w - y
    if x == 3:  # 서
        return w + h + w + h - y
    if x == 4:  # 동
        return w + y

# 입력
w, h = map(int, input().split()) #총 가로세로 길이 입력
n = int(input()) #상점 개수 입력

# 풀이
course = []
for _ in range(n + 1):  # 북쪽 (0) 에서 상점까지의 거리
    x, y = map(int, input().split())
    course.append(get_distance(x, y))

answer = 0

for i in range(n):  # 동근이와 상점 사이의 최단거리
    in_course = abs(course[-1] - course[i]) #정방향으로 거리를 구할때의 거리차를 구한다.
    out_course = 2 * (w + h) - in_course #반대로 거리를 구할때의 거리차를 구한다.
    answer += min(in_course, out_course) # 그 두개중 작은 값을 더해준다.

# 출력
print(answer)

'''
w, h = map(int, input().split()) # 가로, 세로 길이
n = int(input()) # 상점 개수
store = []
for s in range(n): # 상점 위치 저장
   a, b = map(int, input().split())
   store.append([a, b])
dongDirec, dongFar = map(int, input().split()) # 동근이 위치

ans = 0
direc, far = 0, [] # 상점 변수
dFar = []
if dongDirec == 1 or dongDirec == 2:
   dFar = [dongFar, abs(dongFar-w)]
else:
   dFar = [dongFar, abs(dongFar-h)]

for i in range(n):
   tmp = []

   direc = store[i][0] # 상점 방향 
   if direc == 1 or direc == 2: # 상점 위치
      far = [store[i][1], abs(w-store[i][1])]
   else:
      far = [store[i][1], abs(h-store[i][1])]
   
   for s in far:
      for d in dFar:
         tmp.append(s+d)

   if direc == dongDirec:
      if direc == 1 or direc == 2:
         ans += abs(dongFar-store[i][1])
      else:
         ans += abs(dongFar-store[i][1])
   else:
      if dongDirec == 1 or dongDirec == 2:
         if direc == 3:
            ans += 
   print(tmp, ans)

print(ans)
'''
'''
     1=북
3=서      4=동
     2=남
'''