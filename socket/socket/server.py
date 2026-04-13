import socket

server=socket.socket()

server.bind(('localhost', 12345))

server.listen(1)
print("Server Waitting for Connection...")

conn, addr = server.accept()
print("Connected With: ", addr)

data=conn.recv(1024).decode()

num1, num2 = map(int, data.split())

result = num1 + num2

print("received number:", num1, num2)
print("Result is:", result)

conn.close()
server.close()