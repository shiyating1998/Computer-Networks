from __future__ import print_function
from socket import *
import sys

#Input: <server_address> address of the server,
#       <n_port> port used in the negotiation stage,
#       <req_code> validation code for receiving a valid port number
#                  for the transaction stage
#       <msg>      text message send to the server to add to the list of
#                  message of terminate 

server_address = "127.0.0.1"
n_port = 12000
req_code = 1234
msg = 'test'

LOG_FILENAME = 'client.txt'

#validate_ip(s)
#Input: String s - ipAddr
#Output: Boolean, true if s is an IPAddr, False otherwise
#helper function is determining whether string s is an IPaddr
def validate_ip(s):
    a = s.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True

#check for parameters
if (len(sys.argv)>4):   
    
    #get server address
    string = sys.argv[1]
    if (validate_ip(string)):
        server_address = string
       # print(server_address)
    else:
        print ("Invalid IP address\n")
        #exit()
        
    #get n_port
    string = sys.argv[2]
    if (string.isdigit()):
        n_port = int(string)
       # print(n_port)
    else:
        print ("Invalid n_port\n")
        exit()
        

    #get req_code
    string = sys.argv[3]
    if (string.isdigit()):
        req_code = int(string)
       # print(req_code)
    else:
        print ("Invalid request code\n")
        exit()
        

    #get msg 
    msg = sys.argv[4]
    
else:
    print ("Wrong number of parameters given\n")
    exit()


#build TCP connection for negotiation 
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((server_address, n_port))

clientSocket.send(str(req_code).encode())

r_port = clientSocket.recv(1024).decode()
message = "r_port: " + r_port
#print(message)

r_port = int(r_port)
if (r_port == 0):
    #terminate with an error, print to stderr
    print("Invalid req_code\n", file=sys.stderr)
    clientSocket.close()
    
    f = open(LOG_FILENAME,'a')
    f.write("Invalid req_code\n")
    f.close()
    
    input("Press any key to exit...")
    #exit with non-zero exit code 
    exit(1)
    

#add r_port to the log file 
f = open(LOG_FILENAME,'a')
f.write(message)
f.close()


#close the negotiation socket 
clientSocket.close()

#create a UDP clientSocket for transaction stage at r-port 
clientSocket = socket(AF_INET, SOCK_DGRAM)


clientSocket.connect((server_address ,r_port))        
  
#send GET request
clientSocket.send("GET".encode())

message = ''
while True:
    m = clientSocket.recv(1024).decode()
    message += m + '\n'
    if ( m=="NO MSG"):
        ##print("no msg received.\n");
        break
    
print(message)

f = open(LOG_FILENAME,'a')
f.write(message+"\n")
f.close()

#send msg to the server
clientSocket.send(msg.encode())


#waits for keyboard input before exiting
input("Press Enter to exit...\n")
clientSocket.close()

