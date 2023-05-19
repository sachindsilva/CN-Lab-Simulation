import socket

HOST="localhost"
PORT=7999

with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:
    s.bind((HOST,PORT))

    print("Server is running...")

    while True:
        receiveData,addr=s.recvfrom(1024)
        message=receiveData.decode()
        print(f"From client : {addr[0]} : {addr[1]} = {message}")

        modified_msg=message.upper()
        sendData=modified_msg.encode()
        
        s.sendto(sendData,addr)
        
        print("Data sent successfully..")
        