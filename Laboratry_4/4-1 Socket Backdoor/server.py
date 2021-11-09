#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import os
import platform

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем сокет
sock.bind(('', 55000))  # связываем сокет с портом, где он будет ожидать сообщения
sock.listen(10)  # указываем сколько может сокет принимать соединений
print('Server is running, please, press ctrl+c to stop')
while True:
    conn, addr = sock.accept()  # начинаем принимать соединения
    print('connected:', addr)  # выводим информацию о подключении
    data = conn.recv(1024)  # принимаем данные от клиента, по 1024 байт
    print(str(data))

    if data == "hostname -I" :
        # conn.send(platform.platform())
        send_message(platform.platform(), conn)
    elif data == "uname -a" :
        # conn.send(socket.gethostname())
        send_message(platform.platform(), conn)
    elif data == "quit" :
        conn.close()
    
conn.close()  # закрываем соединение

# send_message отправляет сообщение клиенту на принятый сокетный коннект
def send_message(message, my_socket):
    my_socket.send(bytes(message, encoding = 'UTF-8'))