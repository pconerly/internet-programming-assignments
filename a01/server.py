import socket

host = ''
port = 50000
backlog = 5
size = 1024
s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)
while True:
    client, address = s.accept()
    data = client.recv(size)
    if data:
        mid = data.find(',')
        answer = int(data[:mid]) + int(data[mid+1:])
        client.send(str(answer))
        client.close()

