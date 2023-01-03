#
list1 = []
list2 = []

for i in range(10):
    a = int(input())
    list1.append(a)

for i in range(10):
    a = list1[i] % 42
    list2.append(a)
    set1 = set(list2)

print(len(set1))
