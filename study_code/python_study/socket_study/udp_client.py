import socket

HOST = '127.0.0.1'
PORT = 3434

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

data = "Hello UPD!"
s.sendto(data, (HOST, PORT))
print("Sent: %s to %s:%d" % (data, HOST, PORT))
s.close()