import socket
import datetime

HOST = '0.0.0.0'
PORT = 3434

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

while True:
    conn, addr = s.accept()
    print("Clent %s connected!" % str(addr))
    dt = datetime.datetime.now()
    message = "Current time is " + str(dt)
    conn.send(message)
    print("Sent: ", message)
    conn.close()
