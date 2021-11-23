import hashlib
import socket


def store(d):
    with open("/tmp/out", "a+") as h:
        h.write(d + "\n")


def encrypt(p):
    return hashlib.sha512(p).hexdigest()


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 10001))
sock.listen(1)

while True:
    conn, _ = sock.accept()

    while True:
        data = conn.recv(1024)
        if not data:
            break

        data = data.rstrip()
        login, passwd = data.split(" ")
        store(login + " " + encrypt(passwd))
    conn.close()
