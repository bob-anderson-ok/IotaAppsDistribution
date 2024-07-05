# This code demonstrates how to send a command to the IotaGFTapp.
# We do not currently expect SharpCap to control the IotaGFTapp which deals better with scheduling
# start of recording and flash timing than SharpCap.
# We leave this script in place for future reference if a use-case can be made for SharpCap
# sending such commands to IotaGFTapp

import socket, os

def flashNow():
	HOST = '127.0.0.1'
	PORT = 33001
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))
		msg = makeMsg('flash now')			# Make the command string MSGLEN in length
		s.sendall(msg)						# Send the command
		_, ans = getResponse(s)				# Get the response
		ans = msgTrim(ans.decode("utf-8")) 	# Turn bytes into string characters
		print('Sent:', 'flash now')
		if ans == "OK":
			print("Rcvd:", ans)
		else:
			print("ERR!:", ans)
flashNow()