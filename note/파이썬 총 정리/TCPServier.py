import socket
import threading

def start_server():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()

    print(f"서버가 {host}:{port}에서 대기 중...")

    # 클라이언트를 저장할 리스트와 락
    client_sockets = []
    client_addresses = []
    client_lock = threading.Lock()

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"{client_address}에서 연결이 수락되었습니다.")

        # 클라이언트에게 연결 완료 메시지 전송
        welcome_message = "서버에 연결되었습니다. 채팅을 시작하세요!"
        client_socket.send(welcome_message.encode('utf-8'))

        # 클라이언트 소켓과 주소를 리스트에 추가
        with client_lock:
            client_sockets.append(client_socket)
            client_addresses.append(client_address)

        # 채팅 시작을 위한 스레드 시작
        threading.Thread(target=chat_with_client, args=(client_socket, client_lock, client_sockets)).start()

def chat_with_client(client_socket, client_lock, client_sockets):
    while True:
        try:
            # 클라이언트로부터 메시지 수신
            message = client_socket.recv(1024).decode('utf-8')
            print(f"클라이언트: {message}")

            # 종료 명령 확인
            if message.lower() == 'exit':
                break

            # 서버가 클라이언트에게 메시지 전송
            server_message = input("서버: ")

            # 종료 명령 확인
            if server_message.lower() == 'exit':
                broadcast(server_message, client_lock, client_sockets)
                break

            broadcast(server_message, client_lock, client_sockets)
        except Exception as e:
            print(f"에러 발생: {e}")
            break

    # 채팅 종료 시 클라이언트 소켓을 리스트에서 제거
    with client_lock:
        client_sockets.remove(client_socket)

def broadcast(message, client_lock, client_sockets):
    # 모든 클라이언트에게 메시지 전송
    with client_lock:
        for client_socket in client_sockets:
            try:
                client_socket.send(message.encode('utf-8'))
            except Exception as e:
                print(f"에러 발생: {e}")

if __name__ == "__main__":
    start_server()
