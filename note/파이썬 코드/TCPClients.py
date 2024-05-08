import socket
import threading

def start_client():
    server_host = '127.0.0.1'
    server_port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))
    print(f"서버에 {server_host}:{server_port}로 연결되었습니다.")

    # 서버로부터 연결 완료 메시지 수신
    welcome_message = client_socket.recv(1024).decode('utf-8')
    print(welcome_message)

    # 채팅 시작
    threading.Thread(target=receive_messages, args=(client_socket,)).start()
    send_messages(client_socket)

def receive_messages(client_socket):
    while True:
        try:
            # 서버로부터 메시지 수신
            message = client_socket.recv(1024).decode('utf-8')
            print(f"서버: {message}")

            # 종료 명령 확인
            if message.lower() == 'exit':
                break
        except Exception as e:
            print(f"에러 발생: {e}")
            break

def send_messages(client_socket):
    while True:
        try:
            # 사용자로부터 메시지 입력
            user_input = input("클라이언트: ")

            # 종료 명령 확인
            if user_input.lower() == 'exit':
                client_socket.send(user_input.encode('utf-8'))
                break

            # 서버에 메시지 전송
            client_socket.send(user_input.encode('utf-8'))
        except Exception as e:
            print(f"에러 발생: {e}")
            break

if __name__ == "__main__":
    start_client()
