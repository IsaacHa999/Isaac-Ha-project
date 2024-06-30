def simple_coroutine():
    print('Coroutine started')
    x = yield
    print(f'Coroutine received: {x}')

# 코루틴 생성
coroutine = simple_coroutine()

# 코루틴 실행 시작
next(coroutine)  # 'Coroutine started' 출력

# 코루틴에 값 전달 및 재개
coroutine.send(10)  # 'Coroutine received: 10' 출력
