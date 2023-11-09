# 클새스의 상속 : 조상(부모) 클래스의 멤버(필드, 메서드, 생성자) 등르 자손 클래스가 물렵다아 새로우 ㄴ클래스를 만드느 것이다. 
# 조상클래스의 멤버가 자손클래스에 영향을 준다
# 자손클래스의 변화는 조상클래스에 영향을 끼치지 아니한다. 

#조상클래스
class Car: 
    speed = 0
    door = 0
    
    def __init__(self):
        pass
    
    def upSpeed(self, speed):
        self.speed += speed
        print("현재속도(조상클래스) : %d" % self.speed)
        print("문의 개수(조상클래스) : %d" % self.door)
        
        

#자손클래스
class Sedan(Car):
    def __init__(self,speed,door):
        #조상클래스의 생성자를 호출하는 부분이다.
        Car.__init__(self)
        self.speed = speed
        self.door = door
    
    def downSpeed(self, speed):
        self.speed -= speed
        print("현재속도(자손클래스) : %d" % self.speed)

if __name__ == "__main__":
    car = Car()
    car.upSpeed(50)
    print("--------")
    print("car 주소 : ", id(car))
    
    
    sedan = Sedan(100,4)
    print("sedan 주소 : ", id(sedan))
    sedan.upSpeed(150)
    sedan.downSpeed(100)
    
