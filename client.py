import socket
from threading import Thread

HOST = "127.0.0.1"
PORT = 12345

nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
client.sendall(b"Hello server")

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occured!")
            client.close()
            break

def write():
    while True:
        input_message = input('')
        if input_message == ':q':
            client.close()
        message = '{}: {}'.format(nickname, input_message)
        client.send(message.encode('ascii'))

receive_thread = Thread(target=receive)
receive_thread.start()

write_thread = Thread(target=write)
write_thread.start()
