# 4
# . 리 스 트에 1 이 1 개 2 가 2 개 3 이 3 개 ……, N 이 N 개 가 들 어 있 을 수 있 도 록 프 로 그 램 을 작 성 하 시오 단
# 3 번 문 제 와 같 이 N 은 입 력 받 지 않 고 사 용 자가 임 의로 값 을 지 정 한 다

inint = 10
a = list()
for i in range(1,inint+1):
    list1 = [i]*i
    a = a+list1
    
print(a)