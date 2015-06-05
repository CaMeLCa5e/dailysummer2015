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
