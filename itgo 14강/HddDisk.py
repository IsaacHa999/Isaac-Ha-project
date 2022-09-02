from Disk import *
# 자손클래스 정의 
class HddDisk(Disk):
    __capacity = 0
    __rpm = 0
    
    def __init__(self, capacity, rpm):
        Disk.__init__(self, capacity, rpm)
        self.__capacity = capacity
        self.__rpm = rpm

    def getCapacity(self):
        return self.__capacity
    
    def getRpm(self):
        return self.__rpm

    def showPrint(self):
        return "HDD 디스크의 용량은 " + str(self.__capacity) + "GB 이며" \
            "RPM은" + str(self.__rpm) + "입니다." 