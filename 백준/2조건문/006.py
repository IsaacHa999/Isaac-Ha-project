# % // 해석!!!

hour = 0
min = 0

a, b  = map(int, input("").split())
c = int(input())

k = (b+c)//60
hour = a+k
min = b+c

if hour >= 24:
    hour = hour % 24

if (b+c) >=60:
    min = (b+c) % 60
print(hour, min)