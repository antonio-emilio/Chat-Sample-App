from socket import *
import sys
import pickle
import threading
import const

# This class defines the code run by the receiving thread
class RecvHandler(threading.Thread):
    def __init__(self, sock):
        threading.Thread.__init__(self)
        self.client_socket = sock

    def run(self):
        while True:
            (conn, addr) = self.client_socket.accept()
            marshaled_msg_pack = conn.recv(1024)
            msg_pack = pickle.loads(marshaled_msg_pack)
            print("\nMESSAGE FROM: " + msg_pack[1] + ": " + msg_pack[0])
            conn.send(pickle.dumps("ACK"))
            conn.close()
        return

# Configure the address of the local user
try:
    me = str(sys.argv[1])
except:
    print('Usage: python3 chatclient.py <Username>')
    exit(1)

# Check if user exists in the registry
if me not in const.registry:
    print(f"User '{me}' does not exist. Please provide the IP and port for the user.")
    ip = input("Enter IP: ")
    port = int(input("Enter Port: "))

    # Update the registry with the new user's information
    const.registry[me] = (ip, port)
    # Save the updated registry to the const.py file
    with open("const.py", "w") as file:
        file.write(f"CHAT_SERVER_HOST = \"{const.CHAT_SERVER_HOST}\"\n")
        file.write(f"CHAT_SERVER_PORT = {const.CHAT_SERVER_PORT}\n")
        file.write("\n")
        file.write("registry = {\n")
        for user, (user_ip, user_port) in const.registry.items():
            file.write(f"    \"{user}\": (\"{user_ip}\", {user_port}),\n")
        file.write("}\n")
        print(f"User '{me}' has been added to the registry.")

client_sock = socket(AF_INET, SOCK_STREAM)
my_port = const.registry[me][1]
client_sock.bind(('0.0.0.0', my_port))
client_sock.listen(5)

# Put receiving thread to run
recv_handler = RecvHandler(client_sock)
recv_handler.start()

# Get initial destination
dest = input("ENTER DESTINATION ('exit' to quit): ")

# Handle loop for user interaction (in the main thread)
while True:
    msg = input("ENTER MESSAGE: ")

    if msg.lower() == "exit":
        dest = input("ENTER DESTINATION ('exit' to quit): ")
        if dest.lower() == "exit":
            break

    try:
        server_sock = socket(AF_INET, SOCK_STREAM)
        server_sock.connect((const.CHAT_SERVER_HOST, const.CHAT_SERVER_PORT))

        msg_pack = (msg, dest, me)
        marshaled_msg_pack = pickle.dumps(msg_pack)
        server_sock.send(marshaled_msg_pack)
        marshaled_reply = server_sock.recv(1024)
        reply = pickle.loads(marshaled_reply)
        if reply != "ACK":
            print("Error: Server did not accept the message (dest does not exist?)")
        else:
            pass
        server_sock.close()

    except ConnectionRefusedError:
        print("Server is down. Exiting...")
        exit(1)
