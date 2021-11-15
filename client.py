
from client import TcpConexion, UdpConexion

def main() -> None:
    print('Bienvenido a la Mini Aplicacion de Sistemas Distribuidos')
    print('Desea conectarse al servidor por medio que protocolo:')
    print('.- TCP')
    print('.- UDP')
    res = input()
    ip = "127.0.0.1"
    port = 19876
    # Set the conexion type
    try:
        serverResponse = 'Algo paso mal...'
        print('Introduzca la identificación con el servidor')
        response = input()
        if (res == 'TCP' or res == 'tcp'):
            tcpClient = TcpConexion.TcpConexion(ip, port)
            serverResponse = tcpClient.requestServer(response)

        elif (res == 'UDP' or res == 'udp'):
            udpClient = UdpConexion.UdpConexion(ip, port)
            serverResponse = udpClient.requestServer(response)

        print(serverResponse)
        print('La respuesta del servidor es: '+serverResponse)
        print('Presione enter para cerrar el programa')
        input()
    except Exception as e:
        print(e)
        input()
    
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
        input()