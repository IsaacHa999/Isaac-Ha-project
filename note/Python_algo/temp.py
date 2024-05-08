a, b = map(int, input().split())

if (a > b):
    temp = a
    a = b
    b = temp
count = 0

print(b - a - 1)
for i in range(a+1, b):
    print(i, end = ' ')