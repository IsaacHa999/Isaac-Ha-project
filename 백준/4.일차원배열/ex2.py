# 

N,X = map(int, input().split())  # 10 5
A = list(map(int, input().split()))     # 1 2 3 4 5 6 7 8 8 19
print(A)

for i in range(N):
    if A[i] < X:
        print(A[i], end = " ")
# for i in range(N):
#     a = int(input("숫자입력: "))
#     lista.append(a)

