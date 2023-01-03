## 최대 최소 


N = int(input())  
A = list(map(int, input().split()))    

max = A[0]
min = A[0]

for i in range(len(A)):
    if max < A[i]:
        max = A[i]
for i in range(len(A)):
    if min > A[i]:
        min = A[i]

print(min, max)
