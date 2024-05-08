import turtle

# 거북이 설정
t = turtle.Turtle()
t.speed(2)  # 거북이 속도 설정
t.pensize(3)  # 펜의 두께 설정
t.color("blue")  # 선의 색상 설정

# 사각형 그리기 (집의 바닥)
t.penup()
t.goto(-100, -100)
t.pendown()
for _ in range(4):
    t.forward(200)
    t.left(90)

# 삼각형 그리기 (집의 지붕)
t.penup()
t.goto(-100, 100)
t.pendown()
t.setheading(45)  # 거북이 방향 설정
t.forward(141.4)  # 삼각형의 한 변의 길이는 200루트2이므로 대각선의 길이인 루트2를 곱한다
t.setheading(45)  # 거북이 방향 초기화
t.right(90)
t.forward(141.4)
# t.setheading(135)
# t.forward(200)

# 거북이 숨기기
t.hideturtle()

# 화면 유지
turtle.done()
