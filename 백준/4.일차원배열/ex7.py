#
sum =0

#
a = int(input())

list1 = list(map(int, input().split()))

M = max(list1)

for i in range(a):
    list1[i] = list1[i]/M*100
    
for i in range(a):
    sum += list1[i]
print(sum/a)