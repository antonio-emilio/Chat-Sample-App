from socket import *
import pickle
import const
import threading

server_sock = socket(AF_INET, SOCK_STREAM)
server_sock.bind(('0.0.0.0', const.CHAT_SERVER_PORT))
server_sock.listen(5)

print("Chat Server is ready...")

def handle_client_connection(conn, addr):
    marshaled_msg_pack = conn.recv(1024)
    msg_pack = pickle.loads(marshaled_msg_pack)
    msg = msg_pack[0]
    dest = msg_pack[1]
    src = msg_pack[2]
    print("RELAYING MSG: " + msg + " - FROM: " + src + " - TO: " + dest)

    try:
        dest_addr = const.registry[dest]
    except:
        conn.send(pickle.dumps("NACK"))
        conn.close()
        return

    conn.send(pickle.dumps("ACK"))
    conn.close()

    client_sock = socket(AF_INET, SOCK_STREAM)
    dest_ip = dest_addr[0]
    dest_port = dest_addr[1]
    try:
        client_sock.connect((dest_ip, dest_port))
    except:
        print("Error: Destination client is down")
        client_sock.close()
        return

    msg_pack = (msg, src)
    marshaled_msg_pack = pickle.dumps(msg_pack)
    client_sock.send(marshaled_msg_pack)
    marshaled_reply = client_sock.recv(1024)
    reply = pickle.loads(marshaled_reply)
    if reply != "ACK":
        print("Error: Destination client did not receive message properly")
    client_sock.close()

def start_server():
    while True:
        (conn, addr) = server_sock.accept()
        client_thread = threading.Thread(target=handle_client_connection, args=(conn, addr))
        client_thread.start()
        print("Client connected to server at " + str(addr) + " - Starting thread for client")

start_server()
