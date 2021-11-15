import socket


class UdpConexion:
    def __init__(self, ip, port) -> None:
        self.ip = ip
        self.port = port

    def requestServer(self, message):
        # Create a UDP socket at client side
        UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        try:
            # Send to server using created UDP socket
            UDPClientSocket.sendto(str.encode(message), (self.ip, self.port))

            msgFromServer = UDPClientSocket.recvfrom(1024)
            serverResponse = msgFromServer[0].decode()

            if (serverResponse == 'OK'):
                # TODO Answer for the message
                userName = message.split()[1]
                print('Ingrese el mensaje a enviar:')
                messageToBeSent = userName + ' ' + input()

                UDPClientSocket.sendto(str.encode(messageToBeSent), (self.ip, self.port))
                msgFromServer = UDPClientSocket.recvfrom(1024)
                serverResponse = msgFromServer[0].decode()
            
            return serverResponse
        finally:
            print('Conexion terminada, cerrando socket')
            UDPClientSocket.close()