from socket import *
import sys
from packet import *
import util

#if the seq num in the data packet received is expected
# send seqnum = received packet
#else, discard the received packet, and resend an Ack with previously received
# seqnum

#in the end, send EOT and exit

#receiver should create the destination file if it doesn't exist,
#overwrite if it exists (open the file with w flag)

'''
para1 <hostname for the network emulator>,
para2 <UDP port number used by the emulator to receive ACKs from the
receiver>,
para3 <UDP port number used by the receiver to receive data from the
emulator>, and
para4 <name of the file into which the received data is written>
'''


expectedSeq = 0
receivedPackets = [] #array of received packets
eotReceived = False
logName = "arrival.log"
logseq_num = ""

if (len(sys.argv)>4):   
    
    string = sys.argv[1]
    netAddr = string
    #print("netAddr:"+netAddr)
        
    string = sys.argv[2]
    if (string.isdigit()):
        netPort = int(string)
        #print("netport:" + str(netPort))

    #get receiverPort
    string = sys.argv[3]
    if (string.isdigit()):
        receiverPort = int(string)
        #print("receiverPort:" + str(receiverPort))
   
    #get fileName 
    fileName = sys.argv[4]
    #print("fileName:" + fileName)
    
else:
    print ("Wrong number of parameters given\n")
    #exit()
    
'''socket used to send ACKs'''
sendSocket = socket(AF_INET, SOCK_DGRAM)

'''socket used to receive data'''
receiveSocket = socket(AF_INET, SOCK_DGRAM)
receiveSocket.bind(("", receiverPort))


while (eotReceived == False):
    msg, addr = receiveSocket.recvfrom(1000)
    p = packet.parse_udp_data(msg)
  
    logseq_num += str(p.seq_num)+"\n"
  
    firstP = True

    #if eot received, ack eot 
    if (p.type==2 and p.seq_num == expectedSeq):
        eotReceived = True
        util.sendP(sendSocket, packet.create_eot(p.seq_num),netAddr,netPort)
        
    #if data received, with the expectedSeq, send ack
    elif (p.type==1 and p.seq_num == expectedSeq):
        firstP = False
        receivedPackets.append(p)
        util.sendP(sendSocket, packet.create_ack(expectedSeq),netAddr,netPort)
        if (expectedSeq == 31):
            expectedSeq = 0
        else:
            expectedSeq += 1
        #print("ack:" + str(expectedSeq))
            
    #otherwise, not expected, send the prev received ack
    else:
        if (firstP==False):
            util.sendP(sendSocket, packet.create_ack(expectedSeq-1),netAddr,netPort)
            
#log seq_num
f = open(logName,'w')
f.write(logseq_num)
f.close()
    
#output data received from packets 
line = ""
for i in receivedPackets:   
    line += i.data
f = open(fileName,'w')
f.write(line)
f.close()





