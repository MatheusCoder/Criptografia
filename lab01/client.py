import socket
from numeroPrimo import GeradorNumeroPrimo
from gerarChaves import Chaves
from criptografia import Criptografia

p = GeradorNumeroPrimo()
numero_p = p.numero_primo
print('\n P :',str(numero_p))

q = GeradorNumeroPrimo()
numero_q = q.numero_primo
print('\n Q :',str(numero_q))

chaves = Chaves(numero_p, numero_q)
chaves.gerar_chaves()


def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5013  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input(" -> ")  # take input

    while message.lower().strip() != "bye":
        message.encripta_mensagem(message)
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode() # receive response

        print("Received from server: " + data)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == "__main__":
    client_program()
