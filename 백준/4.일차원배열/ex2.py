## 리스트로 문자를 받는 방법!!!!!


N,X = map(int, input().split())  
A = list(map(int, input().split()))    


for i in range(N):
    if A[i] < X:
        print(A[i], end = " ")

