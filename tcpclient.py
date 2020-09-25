# tcpclient.py
import socket
sentence = input("Please enter words: ")
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(("localhost", 6789))
clientSocket.send(str.encode(sentence))
modifiedSentenceBytes = clientSocket.recv(4096)
modifiedSentence = modifiedSentenceBytes.decode("utf-8")
clientSocket.close()
print(modifiedSentence)
