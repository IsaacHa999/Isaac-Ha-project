class Character:
    # 상수값 정의
    WEEK =0
    NORMAL =10 
    STRONG = 20
    VERY_STRONG = 30
    
    def __init__(self):
        self.__hp = Character.NORMAL
        