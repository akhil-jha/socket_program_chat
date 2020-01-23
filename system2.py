import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 11999

mysocket.connect((ip, port)) # ip from system1.py
flag = 1
while flag == 1:
    message_outbound = input("Enter your message (For exit: exit() ):  ")
    temp = message_outbound.strip(" ")
    temp = temp.split(" ")
    if "exit()" in temp:
        flag = 0
        mysocket.close()
        exit(1)
    else:
        mysocket.send(bytes(message_outbound, "utf-8"))
    message_inbound = mysocket.recv(1024)
    print("Peer message: ", message_inbound.decode("utf-8"), end='\n')
mysocket.close()
