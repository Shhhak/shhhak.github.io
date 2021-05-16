score = int(input())
if(100>=score>=90):
    print("A")
elif(90>score>=80):
    print("B")
elif(80>score>=70):
    print("C")
elif(70>score>=60):
    print("D")
else:
    print("F")
#시험 성적

year = int(input())
if(year % 4 == 0 and year % 100 != 0):
  print(1)
elif(year % 400 == 0):
  print(1)
else:
  print(0)
#윤년 구하기

H,M = map(int, input().split())
if(M>44):
  print(H,M-45)
elif(M<45 and H>0):
  print(H-1,M+15)
else:
  print(23,M+15)
#알람 시계