# 인스턴스가 함수의 인자값으로 전달될 때느 ㄴ함수에서 인스턴스ㅡ이 갑승ㄹ 변경할 수가 있다. 그 이유느 ㄴ인스턴스는 함수에 매개변수로 전달될 때 참조(주소)값이 전달이 되어서 변경이 가능하다.
# 리스트를 생각하면 쉽게 이해가 될 것이다.



# 사각형 클래스 저으이
class Rectangle:
    # side = 0 는 매개변수의 값이 주어지지 아니할 때 0으로 초기화
    def __init__(self, side = 0):
        self.side = side
        
    # 정사각형의 면적을 출력하는 메소드
    def getArea(self):
        return self.side * self.side

#함수를 정의
# 클래스 Rectangle의 인스턴스와 횟수를 매개변수로 받아서 횟수가 값이 0이 될 때까지 변의 길이와 면적을 출력해주는 함수
def printArea(rectangle, cnt):
    print("변의 길이", "\t", "면적")
    while cnt >= 1:
        print(rectangle.side, "\t", rectangle.getArea())
        rectangle.side +=1
        cnt -= 1

if __name__ == "__main__":
    rectangle = Rectangle()
    cnt = 5
    printArea(rectangle, cnt)
    print("정사각형의 한 변의 길이 : ", rectangle.side)
    print("반복 횟수", cnt)