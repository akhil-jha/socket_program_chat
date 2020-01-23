import socket
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 11999
ip = input("Enter IP: ")
mysocket.bind((ip, port))
mysocket.listen(1)
clientsocket, addr = mysocket.accept()
print("Got a connection from %s" % str(addr))
flag = 1
while flag == 1:
    message_inbound = clientsocket.recv(1024)
    print("Peer message: ", message_inbound.decode("utf-8"), end='\n')
    message_outbound = input("Enter your message(For exit: exit() ):  ")
    temp = message_outbound.strip(" ")
    temp = temp.split(" ")
    if "exit()" in temp:
        flag = 0
    else:
        clientsocket.send(bytes(message_outbound, "utf-8"))

mysocket.close()
