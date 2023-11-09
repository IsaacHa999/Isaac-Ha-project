# Phone 클래스의 자손클래스이 ㄴ DmbPhone 클래스 정의
from turtle import color
from Phone import*

class DmbPhone(Phone):
    def __init__(self,model,color,channel):
        # 조상클래스 생성자 호출 2가지 방법
        # 자손클래스 생성자 구현부의 첫 줄에 적어주시길 권장
        Phone.__init__(self)
        self.model = model
        self.color = color
        self.channel = channel

    def turnOnDmb(self):
        print("채널 : ", self.channel, "번 DMB 방송수신을 시작합니다.")

    def turnOffDmb(self):
        print("채널 : ", self.channel, "번 DMB 방송수신을 멉춥니다..")

    def chageChannelDmb(self, channel):
        self.channel = channel
        print("채널 : ", self.channel, "번 DMB 방송수신을 시작합니다.")