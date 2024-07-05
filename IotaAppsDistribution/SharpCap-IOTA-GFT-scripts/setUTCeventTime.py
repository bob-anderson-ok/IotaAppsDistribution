import socket, os
	
def sendUTCeventStartTime():
	HOST = '127.0.0.1'
	PORT = 33001
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))
		msg = makeMsg('setUTCeventTime 2026-01-25 10:11:12')
		s.sendall(msg)						# Send the command
		_, ans = getResponse(s)				# Get the response
		ans = msgTrim(ans.decode("utf-8"))	# Turn bytes into string characters
		print('Sent:', 'setUTCeventTime 2026-01-25 10:11:12')
		if ans == "OK":
			print("Rcvd:", ans)
		else:
			print("ERR!:", ans)

sendUTCeventStartTime()