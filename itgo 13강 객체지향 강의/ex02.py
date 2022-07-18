from Tv import *

if __name__ == "__main__":
    tv1 = Tv()
    tv2 = Tv()
    
    tv1.color = "검정색"
    tv1.powerTv(True,"tv1")
    tv1.channelUp(9,"tv1")
    tv1.volumeUp(25,"tv1")
    tv1.printTv("tv1")
    tv1.powerTv(False,"tv1")
    tv1.volumeUp(30, "tv1")