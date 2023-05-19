import socket
import os

HOST="localhost"
PORT=5000


with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen(1)

    while True:
        print("Waiting for client connection..")

        conn,addr=s.accept()
        
        with conn:
            print("Connection from : ",addr)
            while True:
                filename=conn.recv(1024).decode()
                
                if not filename:
                    break
                print("Requested filename ",filename)

                if not os.path.exists(filename):
                    print("Status : file not found")
                    conn.sendall(b'file not found')
                else:
                    with open(filename) as file:
                        conn.sendall(file.read().encode())
                    print("Status : File transmitted..")
                    break
                
            print("Closing this connection..")