import socket, os

def sendAutorunTrue():
	HOST = '127.0.0.1'
	PORT = 33001
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))
		msg = makeMsg('setAutorunTrue')     # Make the command string MSGLEN in length
		s.sendall(msg)                      # Send the command
		_, ans = getResponse(s)             # Get the response
		ans = msgTrim(ans.decode("utf-8"))  # Turn bytes into string characters
		print('Sent:', 'setAutorunTrue')
		if ans == "OK":
			print("Rcvd:", ans)
		else:
			print("ERR!:", ans)

sendAutorunTrue()