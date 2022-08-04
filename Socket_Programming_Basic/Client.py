
import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((socket.gethostname(), 9906))

msg = c.recv(1024)
print("Recieved Server Response : {}".format(msg.decode("utf-8")))
c.close()
