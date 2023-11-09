from Disk import *
# 자손클래스 정의 
class HddDisk(Disk):
    __capacity = 0
    __rpm = 0
    
    def __init__(self, capacity, rpm):
        Disk.__init__(self, 10, 50)
        self.__capacity = capacity
        self.__rpm = rpm

    def getCapacity(self):
        return self.__capacity
    
    def getRpm(self):
        return self.__rpm

    def showPrint(self):
        return "HDD 디스크의 용량은 " + str(super().getCapacity()) + "GB이며 " \
            "RPM은 " + str(super().getRpm()) + "입니다." 
            
