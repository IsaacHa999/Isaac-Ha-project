# 시작 시각, 필요한 시간(분기준)  -->끝나는 시간
A, B = map(int,input().split())
C = int(input())

C1 = C//60
C2 = C%60


if B+C2 >= 60:
    C1 +=1
    C2,B = 0,0
print(C1, C2)
print(A+C1, B+C2)