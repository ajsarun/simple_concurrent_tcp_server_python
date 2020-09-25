# tcpserver.py
import socket
import threading
def echo_thread_function(connectionSocket):
    clientSentenceBytes = connectionSocket.recv(4096)
    clientSentence = clientSentenceBytes.decode("utf-8")
    connectionSocket.send(str.encode(clientSentence.upper()))
    connectionSocket.close()

welcomeSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
welcomeSocket.bind(("localhost", 6789))
welcomeSocket.listen(5)
while True:
    print("The server is waiting")
    connectionSocket, address = welcomeSocket.accept()
    echoThread = threading.Thread(target=echo_thread_function, args=(connectionSocket,))
    echoThread.start()