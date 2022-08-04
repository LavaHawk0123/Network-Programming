import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 9906))
s.listen(5)
print("looking for connections")
count = 0       # Counter to keep track of client requests
while True:
    c, address = s.accept()
    print("connection established")
    count = count + 1
    c.send(bytes("Server Response : Hello World!",encoding = "utf-8"))
    print("Recieved Request No : {}".format(str(count)))
    print("sent message to server")
