import socket

# 서버와 클라이언트를 위한 함수
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))  # IP 주소와 포트 설정
    server_socket.listen(1)
    print("서버 대기 중...")

    conn, addr = server_socket.accept()
    print("클라이언트와 연결됨:", addr)

    message = conn.recv(1024).decode('utf-8')
    print("수신한 메시지:", message)

    student_id = "20222847"  # 여기에 학번을 입력하세요
    conn.send(student_id.encode('utf-8'))

    conn.close()
    server_socket.close()
    print("서버 종료")

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))  # 서버 IP 주소와 포트 설정

    message = "YongTae zzang!"
    client_socket.send(message.encode('utf-8'))

    server_response = client_socket.recv(1024).decode('utf-8')
    print("서버로부터 받은 응답:", server_response)

    client_socket.close()
    print("클라이언트 종료")

if __name__ == "__main__":
    role = input("서버(S) 또는 클라이언트(C)로 실행하시겠습니까? ").strip().lower()

    if role == 's':
        start_server()
    elif role == 'c':
        start_client()
    else:
        print("유효한 역할을 선택하세요 (S 또는 C).")
