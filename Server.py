import socket
import threading
import os

server = '192.168.0.49'
port = 5000

decision = input("Enable executing command?(Y/N): ").lower() == 'y'

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server, port))
server_socket.listen()

print(f"Server in {server}:{port}")



if decision:
    def receive(conection, address):
        while True:
            try:
                data = conection.recv(1024)
                comand = data.decode()
                result_comand = os.popen(comand).read()
                send(conection, result_comand)
            except Exception as e:
                print(f"Error {e}")
                conection.close()
                break

    def send(conection, result_comand):

        try:
            conection.sendall(result_comand.encode())
        except Exception as e:
            print(f"Error {e}")
            conection.close()

    def conection_up(conection,address):
        print(f"Up with {address}")

        thread_receive = threading.Thread(target=receive, args=(conection,address))
        
        thread_receive.start()
        thread_receive.join()
        print(f"Down with {address}")

else:
    def receive(conection, address):
        while True:
            try:
                data = conection.recv(1024)
                print(f"Message from {address}: {data.decode()}")
            except:
                print("Error")
                conection.close()
                break

    def send(conection, address):
        while True:
            try:
                send = input()
                conection.sendall(send.encode())
            except:
                print("Error")
                conection.close()
                break

    def conection_up(conection,address):
        print(f"Up with {address}")

        thread_receive = threading.Thread(target=receive, args=(conection,address))
        thread_send = threading.Thread(target=send, args=(conection,address))

        thread_receive.start()
        thread_send.start()

        thread_receive.join()
        thread_send.join()

        print(f"Down with {address}")

while True:

    try:
        conection, address = server_socket.accept()
        thread_conection_up = threading.Thread(target=conection_up, args=(conection,address))
        thread_conection_up.start()
        
    except:
        print("Error")