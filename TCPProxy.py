import sys 
import socket 
import threading 
def server_loop(local_host,local_port,remote_host,remote_port,receive_first): 
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try: 
		server.bind((local_host,local_port))
	except: 
		print "[!!] failed to listen"
		print "Checking for other sockets"
		sys.exit(0)
		print "listening on %s:%d"%(local_host,local_port)

		server.listen(5)

		while True:
			client_socket, addr = server.accept()
			print "[==>] Recieved conection from %s: %d" % (addr[0],addr[1])

			proxy_thread = threading.Thread(target=proxy_handler, 
			args=(client_socket,remote_host,remote_port,receive_first))

			proxy_thread.start()

def main():
	if len(sys.argv[1:]) !=5:
		print "Example: .proxy.py 127.0.0.1 9000 10.12.123.1 9000 True"
		sys.exit(0)

	local_host = sys.argv[1]
	local_port = int(sys.argv[2])

	remote_host = sys.argv[3]
	remote_port = int(sys.argv[4])

	receive_first = sys.argv[5]

	if "True" in receive_first: 
		receive_first = True 
	else: 
		receive_first = False

	server_loop(local_host,local_port,remote_host,receive_first)
	
main()