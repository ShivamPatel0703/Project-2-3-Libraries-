import networking
import socket
# We are creating a socket object here for the connection
socketOBJ = socket.socket()
# Get local machine name
localM = socket.gethostname()
# This is the port that we will be working on (in this case it's TCP/UDP netbus)
port = 12345
# We have to use the bind function to activate IP
socketOBJ.bind((localM, port))
# We use the listen function to wait for the client connection (5 seconds)
# The shorter the time waited the less vulnerabilities ((that's why 5)
socketOBJ.listen(5)
# Connection being established
while True:
   connection, address = socketOBJ.accept()
   print('Connection Received From: ', address)
   connection.send('Connection Established ')
   connection.close()
