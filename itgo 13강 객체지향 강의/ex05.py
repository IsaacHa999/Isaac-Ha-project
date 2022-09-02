#문제
#원(circle)을 클래스로 표시해보자. 원은 반지름(radius)을 가지고 있다. 
# 원의 넓이와 둘레를 계산하는 메소드를 정의해보자. 
# 생성자는 매개변수가 존재하는 생성자
# 출력결과
# 원의 반지름 : 10
# 원의 넓이 : 314.16
# 원의 둘레 : 62.83
#-------------------------------------------------------
# is 풀이!!!    굉장히 이상한 경우 많음

# import math
# class Circle:       
#     radius = 0
#     ST = radius * radius * 3.14
#     RT = radius * 3.14 * 2 


    
    
#     def __init__(self, radius):
#         self.radius = radius
#         self.ST = radius * radius * 3.14     #여기서 나오면 안됨 --> 메서드로 값을 만들어야함
#         self.RT = radius * 3.14 * 2 


    
#     def PrintS(self):
#         self.ST = self.radius * self.radius * 3.14
#         print("원의 반지름 : %.2f" % self.radius)
#         print("원의 넓이 : %.2f" % self.ST)
#         print("원의 둘레 : %.2f" % self.RT)
        
# circle1 = Circle(10)                             # 여기도 양식에 맞춰서 할 것 --> 
# circle1.PrintS()

# 신경진tr 풀이

import math
class Circle:
    __radius = 0
    
    # 생성자
    def __init__(self, radius):
        self.__radius = radius
    
    # getter(), setter() 제공
    def getRadius(self):
        return self.__radius
    def setRadius(self, radius):
        self.__radius = radius
    
    # 원의 넓이 구하는 메소드
    def calcArea(self):
        area = math.pi * self.__radius * self.__radius
        return area
    
    # 원의 둘레 구하는 메소드
    def calcCircum(self):
        value = math.pi * self.__radius * 2
        return value 
    
if __name__ == "__main__":
    circle = Circle(10)
    print("원의 반지름 : ", circle.getRadius())
    print("원의 넓이 :", circle.calcArea())
    print("원의 둘레", circle.calcCircum())
        