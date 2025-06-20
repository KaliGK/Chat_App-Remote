import socket
import threading

ip_server = 'IP of the machine used as server'
port = enter port

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip_server, port))


def receive():
    while True:
        
        server = client_socket.recv(1024)
        print(f"Server: {server.decode()}")

def send():
    while True:

        client = input()
        client_socket.sendall(client.encode())

thread_receive = threading.Thread(target=receive)
thread_send = threading.Thread(target=send)

thread_receive.start()
thread_send.start()

thread_receive.join()
thread_send.join()

client_socket.close()
