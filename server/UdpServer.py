import socket

from server.LoggerServerHandler import LoggerServerHandler

class UdpServer(LoggerServerHandler):
    def __init__(self, ip, port, bufferSize) -> None:
        super().__init__()
        self.ip = ip
        self.port = port
        self.bufferSize = bufferSize
        self.usersLogged = []

    def initServer(self) -> None:
        # Create a datagram socket
        UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Bind to address and ip
        UDPServerSocket.bind((self.ip, self.port))

        # Listen for incoming datagrams
        while(True):
            print("Servidor UDP escuchando...")
            try:
                bytesAddressPair = UDPServerSocket.recvfrom(self.bufferSize)

                userMessage = bytesAddressPair[0].decode()
                address = bytesAddressPair[1]

                bytesToSend = str.encode(self.validateUserAndWriteLog(userMessage, 'UDP', address[0]))
                UDPServerSocket.sendto(bytesToSend, address)
                pass
            except Exception as e:
                UDPServerSocket.close()
                print(e)
                break