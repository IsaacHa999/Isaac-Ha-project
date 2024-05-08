import turtle

# 거북이 설정
t = turtle.Turtle()
t.speed(2)  # 거북이 속도 설정
t.pensize(3)  # 펜의 두께 설정
t.color("blue")  # 선의 색상 설정

# 별 모양 그리기
for _ in range(5):
    t.forward(100)  # 앞으로 100 이동
    t.right(144)  # 오른쪽으로 144도 회전

# 거북이 숨기기
t.hideturtle()

# 화면 유지
turtle.done()
