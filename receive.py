##client code
import pickle
import socket
import struct
import cv2

conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# ipv4# Assign an address and a port
server_address = ('192.168.1.186',1234)
conn.connect(server_address)

data = b''
payload_size = struct.calcsize('=L') 

while len(data) < payload_size:
	print('a')
	data += conn.recv(4096)
packed_msg_size = data[:payload_size]
data = data[payload_size:]

## format='=L' for windows and R-pi, for linux it should be 'L'
msg_size = struct.unpack('=L', packed_msg_size)[0]
# Retrieve all data based on message size
while len(data) < msg_size:
	data += conn.recv(4096)    
conn.close()

##convert the data for visualization
frame_data = data[:msg_size]
#print(frame_data)
data = data[msg_size:]
#print(data)
image = pickle.loads(frame_data)
cv2.imshow('image',image)
cv2.waitKey(0)
