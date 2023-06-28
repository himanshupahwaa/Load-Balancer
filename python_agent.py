import socket               # Import socket module
import os
import math
import psutil
s = socket.socket()         # Create a socket object

def get_ip_address():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(("8.8.8.8", 8111))
        return s.getsockname()[0]

ip_address = get_ip_address()
print('ip address is '+ip_address)
port = 3000
def get_server_tier(no_of_cores,total_memory):
   if no_of_cores >= 64 and total_memory >= 124000:
      return 1
   if no_of_cores >= 48 and total_memory >= 62000:
      return 2
   if no_of_cores >= 24 and total_memory >= 30000:
      return 3
   if no_of_cores >= 8 and total_memory >= 7000:
      return 4
   else:
      return 5  
     
server_tier = get_server_tier(psutil.cpu_count(logical = True),psutil.virtual_memory().total >> 20)
#host = socket.gethostname() # Get local machine name
#host = '172.31.18.83'
host = ip_address
#print(host)
port = 4201               # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
print('Success binding host and port')
s.listen(5)                 # Now wait for client connection.
print('Listening')


while True:
   print('Calculating statistics ...')
   c, addr = s.accept()     # Establish connection with client.

   print('Memory Percent: ',psutil.virtual_memory().percent)
   #print('CPU Percent : ',psutil.cpu_percent(percpu = False))
   print('CPU all cores : ',psutil.cpu_percent(percpu = True))
   print('Disk Percent : ',psutil.disk_usage(os.sep).percent)
   
   cpu_percent = psutil.cpu_percent(percpu = False)
   
   free_cpu_percent = 100.0 - cpu_percent
   free_memory_percent = (100.0 - psutil.virtual_memory().percent)
   available_weight = (free_cpu_percent + free_memory_percent)/2
   
   available_weight = math.ceil(available_weight)
   
   print('Free CPU Percent : ',free_cpu_percent)
   
   print('Free Memory Percent : ',free_memory_percent)
   
   print('Server weight : ',available_weight)
   
   weight_according_to_server_tier = (available_weight/server_tier)
   
   print('Server weight according to server tier : ',weight_according_to_server_tier)
   
   my_str = str(math.ceil(weight_according_to_server_tier))+'%\n'
   
   my_str_as_bytes = str.encode(my_str)
   c.send(my_str_as_bytes)
   
   print('Sent weight to load balancer : ',my_str)
   
   c.close()

print('outside for loop')