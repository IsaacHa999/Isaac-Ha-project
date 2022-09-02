# 조상클래스 덩의
class Disk(object):
    __capacity = 0
    __rpm =0
    
    def __init__(self, capacity, rpm):
        self.__capacity = capacity
        self.__rpm = rpm
        
    def getCapacity(self):
        return self.__capacity
    
    def getRpm(self):
        return self.__rpm
    
    def showPrint(self):
        return "디스크의 용량은 " + str(self.__capacity) + "GB 이며" \
            "RPM은" + str(self.__rpm) + "입니다."