import socket

HOST = "localhost"  # The server's hostname or IP address
PORT = 7999  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect((HOST, PORT))
    print("Enter your message here (Type END to stop):")
    
    while True:
        message = input()
        if message == "END":
            break
        else:
            s.sendto(message.encode(), (HOST, PORT))
            data, addr = s.recvfrom(1024)
            modified_msg = data.decode()
            print("From Server:", modified_msg)
