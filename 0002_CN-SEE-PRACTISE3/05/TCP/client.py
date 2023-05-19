import socket

HOST="127.0.0.1"
PORT=5000

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    filename=input("Enter the filename :")

    s.connect((HOST,PORT))

    print("Connected to : ",HOST)

    s.sendall(filename.encode())

    print("Filename sent...")

    data=s.recv(1024).decode()
    
    if data.startswith("file not found"):
        print(f"Requested filename {filename!r} is not found on server {HOST!r}")
    else:
        print(f"Receiving filename : {filename!r}")
        with open(filename,"w") as file:
            while True:
                file.write(data)
                if not data:
                    break
                data=s.recv(1024).decode()
                
        with open(filename,"r") as filer:
            print(filer.readline())
            
        print("DONE.")
    s.close()