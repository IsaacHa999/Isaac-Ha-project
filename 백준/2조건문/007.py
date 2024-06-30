# 주사위 문제

a,b,c = map(int,input("").split())

re = 0
if a == b and b ==c:
    re = 10000 + a*1000
elif a==b or b ==c or c==a:
    if a==b:
        re = 1000 + a*100
    elif a==c: 
        re = 1000 + c*100
    elif b==c:
        re = 1000 + b*100
else: 
    k = max(a,b,c)
    re = k*100


print(re)