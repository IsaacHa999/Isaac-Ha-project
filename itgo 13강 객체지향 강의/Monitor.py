class Monitor:
    # 필드 선언
    company = ""
    inch = 0
    price = 0
    color = ""
    
    # 파이썬에서는 1개 이상의 생성자를 만들수가 없다.
    # 오버로딩 : 같은 메서드명으로 다른 일을 하게끔 만드는 작업
    # 매개변수의 타입과 개수에 따라서 같으 ㄴ이름의 메서드라도 다른 메서드가 호출이 되는 형태를 지칭한다.
    def __init__(self, company, inch, price, color):
        # self.company는 멤버면수를 칭하는 것이며, company는 외부에서 생성자를 호출할 때 매개변수값으로 사용
        self.company = company
        self.inch =inch
        self.price = price
        self.color = color
        
    def __str__(self):
        print("제조사 : ", self.company)
        print("인치 : ", self.inch)
        print("가격 : ", self.price)
        print("색상 : ", self.color)

        
        