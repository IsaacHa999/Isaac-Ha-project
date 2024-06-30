# 평균 구하기
n = input()
mylist = list(map(int, input().split()))    # map() 함수는 리스트의 요소를 지정된 함수로 처리해주는 함수
mymax = max(mylist)
sum = sum(mylist)
print(sum * 100 / mymax / int(n))

# 입력
# 5
# 1 2 4 8 16

# 출력
# 38.75