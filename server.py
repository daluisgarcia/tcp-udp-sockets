import os
from multiprocessing import Process

from server import UdpServer, TcpServer


def main():
    print('Iniciando servidor...')

    ip = "127.0.0.1"
    port = 19876
    bufferSize = 1024

    udpServer = UdpServer.UdpServer(ip, port, bufferSize)
    tcpServer = TcpServer.TcpServer(ip, port, bufferSize)

    udpProcess = Process(target = udpServer.initServer)
    tcpProcess = Process(target = tcpServer.initServer)
    udpProcess.start()
    tcpProcess.start()
    udpProcess.join()
    tcpProcess.join()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
        input()
    