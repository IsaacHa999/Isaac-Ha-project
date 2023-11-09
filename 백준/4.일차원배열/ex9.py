
for i in range(1):
    list1 = list(map(int, input().split()))
    num = list1[0]
    sum = 0
    for k in range(1, len(list1)):
        sum += list1[k]
    print("{0:.3f}%".format(sum/num))