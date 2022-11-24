a = int(input())
b = map(int,input().split())
b = list(b)
c=int(input())


num = 0
for i in range(len(b)):
    if c== b[i]:
        num = num+1
print(num)

