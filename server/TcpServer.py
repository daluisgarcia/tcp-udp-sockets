import socket

from server.LoggerServerHandler import LoggerServerHandler

class TcpServer(LoggerServerHandler):
    def __init__(self, ip, port, bufferSize) -> None:
        super().__init__()
        self.ip = ip
        self.port = port
        self.bufferSize = bufferSize

    def initServer(self) -> None:
        
        # Create a datagram socket
        TCPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Bind to address and ip
        TCPServerSocket.bind((self.ip, self.port))

        TCPServerSocket.listen(1)

        while(True):
            try: 
                # Wait for a connection
                print("Servidor TCP escuchando...")
                connection, client_address = TCPServerSocket.accept()
                # Receive the data in small chunks and retransmit it
                while True:
                    data = connection.recv(self.bufferSize)
                    if data:
                        bytesToSend = str.encode(self.validateUserAndWriteLog(data.decode(), 'TCP', client_address[0]))
                        connection.sendall(bytesToSend)
                        data = None
                        pass
                    else:
                        pass
            except Exception as e:
                TCPServerSocket.close()
                print(e)
                break