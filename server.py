import socket
import logging
from threading import Thread
from db import db 

HOST = "127.0.0.1"
PORT = 12345

clients = []
nicknames = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

def broadcast(message):
    for client in clients:
        client.send(message)

def send_message(socket, message):
    formatted_message = '{}'.format(message)
    message_bytes = formatted_message.encode('utf-8')
    socket.send(message_bytes)

def handle(client, address):
    while True:
        try:
            message = client.recv(1024)
            print(f'{address} said: {message}')
            broadcast(message)
        except:
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        # Accept Connection
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        # Request And Store Nickname
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        # Print And Broadcast Nickname
        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))

        # Start Handling Thread For Client
        thread = Thread(target=handle, args=(client, address))
        thread.start()

receive()
