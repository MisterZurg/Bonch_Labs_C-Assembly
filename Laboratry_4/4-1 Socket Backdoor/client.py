#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем сокет
sock.connect(('localhost', 55000))  # подключемся к серверному сокету

send_message('hostname -I', sock)
recieve_message(sock)  
# Информация о системе
send_message('uname -a', sock)
recieve_message(sock)  
# system(exit)
send_message('quit', sock)
recieve_message(sock)  



sock.close()  # закрываем соединение


# send_message отправляет сообщение на северный сокет
def send_message(message, my_socket):
    my_socket.send(bytes(message, encoding = 'UTF-8'))

# recieve_message печатает ответ от серверного сокета
def recieve_message(my_socket):
    data = sock.recv(1024)
    print(data)    