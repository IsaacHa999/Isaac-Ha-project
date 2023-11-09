alist = []

for i in range(28):
    k = int(input())
    alist.append(k)

alist.sort()

for i in range(1,31):
    if i  not in alist:
        print(i)