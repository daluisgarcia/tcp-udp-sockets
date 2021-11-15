import socket

class TcpConexion:
    def __init__(self, ip, port) -> None:
        self.ip = ip
        self.port = port

    def requestServer(self, message):
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        sock.connect((self.ip, self.port))

        try:
            # Send data
            sock.sendall(str.encode(message))

            # Look for the response
            amount_received = 0
            amount_expected = len(message)

            while amount_received < amount_expected:
                data = sock.recv(1024)
                amount_received += len(data)
                serverResponse = data.decode()

                if (serverResponse == 'OK'):
                    # TODO Answer for the message
                    userName = message.split()[1]
                    print('Ingrese el mensaje a enviar:')
                    messageToBeSent = userName + ' ' + input()
                    sock.sendall(str.encode(messageToBeSent))

                    amount_received = 0
                    amount_expected = len(message)
                    
                    while amount_received < amount_expected:
                        data = sock.recv(1024)
                        amount_received += len(data)
                        serverResponse = data.decode()
                
                return serverResponse

        finally:
            print('Conexion terminada, cerrando socket')
            sock.close()