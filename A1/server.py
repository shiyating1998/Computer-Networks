from socket import *
import sys

#Input: <req_code> used to validate clients attempting to connect


#CONSTANTS
NO_MSG = "NO MSG"
LOG_FILENAME = 'server.txt'

#Global Variable
listOfMsg = ""
req_code = 1234

#req code from para
if (len(sys.argv)>1):
    string = sys.argv[1]
    if (string.isdigit()):
        req_code = int(string)
        #print(req_code)
    else:
        print ("Invalid request code,default request code used")
        #exit()
else:
    print ("No req_code given,default request code used")
    #exit()


#opens TCP server socket for waiting incoming requests 
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', 0))

#find the n_port of the server socket
n_port = serverSocket.getsockname()[1]
msg = "[SERVER_PORT]: " + str(n_port)
print(msg)

#log the server port 
f = open(LOG_FILENAME,'w')
f.write(msg + "\n")
f.close()


serverSocket.listen(100)
'''to be fixed..how many to listen to?'''

#print("The server is ready to receive")
while True:
    #connection socket receives the request code 
    connectionSocket, addr = serverSocket.accept()
    client_req_code = int(connectionSocket.recv(1024).decode())
    
    #if the request code is valid, find a r_port for the transaction stage
    if (req_code == client_req_code):
        #UDP socket
        UDPserverSocket = socket(AF_INET, SOCK_DGRAM)
        UDPserverSocket.bind(('', 0))
        r_port = UDPserverSocket.getsockname()[1]
        #msg = "r_port: " + str(r_port)

        #connection socket sends the r_port to the client for UDP transaction
        connectionSocket.send(str(r_port).encode())
        #print (msg)        
        connectionSocket.close()

        flag = True
        while (flag):
            message, clientAddress = UDPserverSocket.recvfrom(1024)
            message = message.decode()
            #print(message)

            #print the listOfMsg    
            if (message == "GET"):                            
                #print(listOfMsg)           
                UDPserverSocket.sendto(listOfMsg.encode(), clientAddress)
                UDPserverSocket.sendto(NO_MSG.encode(), clientAddress)
                
            #TERMINATE the server
            elif (message == "TERMINATE"):                
                #shut down the server
                serverSocket.close()                
                exit()
                
            #add the new msg to the message list 
            else:              
                msg = "%d: " % (r_port) + message
                #print(msg)
                listOfMsg += "\n" + msg
                UDPserverSocket.close()
                flag = False     
    #if the req code is invalid, send 0 to indicate error               
    else:
        replyMsg = '0'
        connectionSocket.send(replyMsg.encode())
        connectionSocket.close()
        print("req_code not valid")
    
    
