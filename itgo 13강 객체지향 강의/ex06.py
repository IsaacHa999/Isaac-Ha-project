# 문제 
# 은행 계좌에 돈을 저금할 수 있고 인출을 할 수도 있다. 은행 계좌를 간단하게 클래스로 저으이해보다. 
# 은행계좌(Accout)는 현재 잔액(balance)을 필드로 선언하고 기본 생성자를 작성하고 입금(deposit) 메소드와 출금(withdraw) 메소드를 작성해보다.
# 출력결과
# 통장에 1,000,000원이 입금됨
# 현재잔액 : 1,000,000원
# 통장에 200,000원이 출금됨
# 현재잔액 : 8000,000원
# -----------------------------------------------------
class Account:
    __balance = 0
    
    # 생성자
    def __init__(self):
        self.__balance = 0

        
    # getter(), setter()
    def getAccount(self):
        return self.__balance
        # val1 = self.__balance
        # print("현재잔액 :", val1)

        
    # 입금 메소드
    def PlusAccount(self, v1):
        self.__balance += v1
        print("통장에 %d원이 입금됨" % v1)
        print("현재잔액 : %d" % self.__balance)
        
    # 출금 메소드
    def MinusAccount(self, v2):
        self.__balance -= v2
        print("통장에 %d원이 출금됨" % v2)
        print("현재잔액 : %d" % self.__balance)

if __name__ == "__main__":
    account1 = Account()
    account1.PlusAccount(20000)
    account1.MinusAccount(1000)
    