# 가격 개수
re = int(input())
count = 0
num = int(input())

for i in range(num):
    a, b = map(int,input().split())
    sum = a*b
    count +=sum

if re == count:
    print("Yes")
else:
    print("No")
    
