# def server_loop():
# 	global target 

# 	if not len(target): 
# 		target = "0.0.0.0"

# 	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 	server.bind((target, port))

def client_handler(client_socket): 
	global upload
	global execute
	global command 

	if len(upload_destination): 
		file_buffer = ""

		while True:
			data = client_socket.recv(1024)

			if not data:
				break
			else:
				file_buffer += data

		try: 

			file_descriptor = open(upload_destination,"wb")
			file_descriptor.write(file_buffer)
			file_descriptor.close()

			client_socket.send("saved file")
		except: 

			client_socket.send("failed to save file")

	if len(execute): 
		output = run_command(execute)

		client_socket.send(output)

	if command: 

		while True:
			client_socket.send("<BHP:#>")
				(enter key)
			cmd_buffer = ""
			while "\n" not in cmd_buffer: 
				cmd_buffer += client_socket.recv(1024)

			response = run_command(cmd_buffer)
			client_socket.send(response)
