import pyfiglet
from datetime import datetime
import socket,sys,time
import threading
from queue import Queue

class PortScanner(object):
 	"""docstring for PortScanner"""
 	def __init__(self,target,thread=4):
 		self.Banner("PortScanner")
 		self.print_lock = threading.Lock()
 		self.target = target
 		self.q = Queue()
 		self.thread = thread
 		self.port = 0
 		# self.show_closed_port = show_closed_port
 		self.start = time.time()
 		


 	def Banner(self,name):
 		banner = pyfiglet.figlet_format(name )
 		print(banner)
 		print("-"*50)

 	def portscanner(self,port):
 		
 		
 		try:

 			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 			socket.setdefaulttimeout(1) 
 			result = s.connect_ex((self.target,port))
 			with self.print_lock:
 				if result ==0:
 					print(f"Port {port} is open")

 			s.close() 

 		except KeyboardInterrupt:
 			print("\n Exitting Program !!!!") 
 			sys.exit()

 		except socket.gaierror: 
 			print("\n Hostname Could Not Be Resolved !!!!") 
 			sys.exit()

 		except socket.error: 
 			print("\ Server not responding !!!!") 
 			sys.exit()
 		

 	def threader(self):

 		while True:
 			port = self.q.get()
 			self.portscanner(port)
 			self.q.task_done()

 	
 	def main(self):
 		for x in range(self.thread):
 			t = threading.Thread(target=self.threader) 
 			t.daemon = True
 			t.start()
 		start = time.time()
 		for port in range(1,65535):
 			self.q.put(port)
 		self.q.join()
 		print('Time taken:', time.time() - self.start) 
 		print("-"*50)
