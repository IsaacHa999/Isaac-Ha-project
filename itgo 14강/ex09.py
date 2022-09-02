# 메소드 오버라이딩 : 
# 선언부 동일 구현부 다름



# 조상클래스 정의
class Car:
    __speed = 0 
    def upSpeed(self, speed):
        self.__speed +=speed
        print("편재속도(조상클래스) : %d" % self.speed)

class Sedan(Car):
    #메서드 오버라이딩
    def __upSpeed(self,speed):
        self.speed += speed
        if self.speed > 150:
            self.speed = 150
            print("현재속도(자손클래스) : %d" % self.speed)
# 자손클래스 Truck의 정의
class Truck(Car):
    # 구현부에 pass 를 적으면, 조상클래스의 멤버만 상속받고 자신의 멤버는 추가하지 않겠다.
    pass

#---------------------------------------------------------------
if __name__ =="__main__":
    seda1 = None
    truck1 = None
    
    sedan1 = Sedan()
    truck1 = Truck()
    print("승용차의 속도 : ", end = " ")
    sedan1.upSpeed(200)