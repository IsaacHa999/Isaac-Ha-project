alist = []

for i in range(1,10):
    k = int(input())
    alist.append(k)

alist.sort()
print(alist)

for i in range(1,10):
    if i  not in alist:
        print(i)