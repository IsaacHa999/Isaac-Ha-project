from Person import*

if __name__ == "__main__":
    # 기본 생성자 호출
    # 기본 생성자는 호출되면 무조건 똑같으 ㄴ초기값을 지니고 메모리에 생성된다. 그리고 그 겂을 면경하려면 setter() 나 인스턴스.변수명 = 값을 통해 변경한다.
    person1 = Person()
    person1.__str__()

    person2 = Person()
    person2.__str__()
    print("---------------------")
    print("person1.name : ", person1.getName())
    person1.setName("김길동")
    person1.name = "하이삭"
    person1.age = 50
    print("person1.name : ", person1.getName())
    print("person1.address : ", person1.getAddress())
    print("person1.age : ", person1.age)

    # print("person1의 주소: ", id(person1))
    # print("person2의 주소: ", id(person2))