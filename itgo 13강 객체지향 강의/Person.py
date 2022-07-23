# 생서자에 대하 닛ㄹ습
# 개념 : 인스턴스를 생성하기 위해서 꼭 필요한 존재이다.
# 아울어 필드의 초기화 메서드 역할을 한다.
#__init__() 작성해줌으로써 생성자가 호출이 된다.
# 만약에 클래스에 생성자가 존재하지 않으면 인터프리터가 알아서 하나의 기본생성자를 추가해준다. 
class Person:
    name = ""
    age = 0
    height = 0
    weight = 0
    address = ""
    # 기본생성자를 작성함
    def __init__(self):
        self.name = "홍길동"
        self.age = 35
        self.height = 175
        self.weight = 70
        self.address = "경북"
        print("Person의 기본 생성자 호출")
    # getter()는 리턴값만 존재하고 매개변수는 존재하지 않는다.
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getHeigth(self):
        return self.height
    def getWeigth(self):
        return self.weight
    def getAddress(self):
        return self.address
    
    # setter()
    def setName(self, name):
        self.name = name
    # __str()__ 멤버면수의 값을 간단하게 확인하고자 할 때 사용하면 편리하다
    def __str__(self):
        print(self.name)
        print(self.age)
        print(self.height)
        print(self.weight)
        print(self.address)
        