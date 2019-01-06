import socket

HOST = '0.0.0.0'
PORT = 3434

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))

while True:
    data, addr = s.recvfrom(1024)
    print("Received: %s from %s" % (data, str(addr)))

s.close()