import socket

HOST = "localhost"  # The server's hostname or IP address
PORT = 7999  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print("Server Running")

    while True:
        receiveData, addr = s.recvfrom(1024)
        message = receiveData.decode()
        print(f"From Client {addr[0]}:{addr[1]}: {message}")
        modified_msg = message.upper()
        sendData = modified_msg.encode()
        s.sendto(sendData, addr)
        print("Data Sent Successfully")
