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

encripta = chaves.encripta_mensagem()
chaves.decripta_mensagem(encripta)

def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5013  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024by
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        data = input(" -> ")
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == "__main__":
    server_program()
