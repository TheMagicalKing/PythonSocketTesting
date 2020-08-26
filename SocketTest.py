import socket

def ConnectToJava():
    s = socket.socket()
    port = 8192
    host = '10.200.161.30'

    s.connect((host, port))
    s.sendall(b'hello world!')
    data = s.recv(1024)
    print('Received', repr(data))
    s.close()




if __name__ == '__main__':
    ConnectToJava()