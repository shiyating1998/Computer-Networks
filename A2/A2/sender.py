from socket import *
import sys
import threading
from packet import *
import time
import util


#para1 <host address of the network emulator>
#para2 <UDP port number used by the emulator to receive data from the sender>
#para3 <UDP port number used by the sender to receive ACKs from the emulator>
#para4 <name of the file to be transferred>


N = 10

timeOut = 100 #100ms
packetLen = 500 #500bytes of data
ack = -1
numOfPackets = 0 

if (len(sys.argv)>4):
    #get netAddr
    string = sys.argv[1]

    netAddr = string
    print("netAddr:"+netAddr)
    #else:
       # print ("Invalid IP address\n")
        #exit()
        
    #get netPort
    string = sys.argv[2]
    if (string.isdigit()):
        netPort = int(string)
        print("netport:" + str(netPort))
    else:
        print ("Invalid netPort\n")
        #exit()
        

    #get senderPort
    string = sys.argv[3]
    if (string.isdigit()):
        senderPort = int(string)
        print("senderPort:" + str(senderPort))
       # print(req_code)
    else:
        print ("Invalid senderPort\n")
        #exit()
        

    #get fileName 
    fileName = sys.argv[4]
    print("fileName:" + fileName)
    
else:
    print ("Wrong number of parameters given\n")
    #exit()


#read data from the file 
packetList = [] #array of packets with data
f = open(fileName, 'r')
data = f.read(500)

seqnum = 0
while(data):
    p = packet.create_packet(seqnum,data)
    packetList.append(p)
    numOfPackets += 1
    data = f.read(500)
    if seqnum==31:
        seqnum = 0
    else:
        seqnum = seqnum+1
    #print("seqnum: " + str(seqnum))
f.close()


seqnum = 0

def resendPackets():
    while (util.eotReceived!=True):
        #print("resent Packet\n")
        global t3
        t3.cancel()
        t3 = threading.Timer(0.1,resendPackets)
        t3.start() 
        sendSocket = socket(AF_INET, SOCK_DGRAM)
        count = util.base
        
        num = util.nextseqnum
        #print("count:" + str(count)+"\n")
        #print("num:" + str(num)+"\n")
        while(count< num):
            util.sendP(sendSocket,packetList[count],netAddr,netPort)
            count+=1
            

def send_data():
    global t3
    #UDP socket to send data
    sendSocket = socket(AF_INET, SOCK_DGRAM)
    #log seqnum.log

    while (util.eotReceived!=True):
        #all packets been sent, send the eot
        if (util.nextseqnum == numOfPackets and util.base == util.nextseqnum):
            p = packet.create_eot(seqnum%32)
            #print("eotsent")
            #print("seqnum:" + str(seqnum))
            #print("seqnum%32:" + str(seqnum%32))
            util.sendP(sendSocket,p,netAddr,netPort)
            t3.cancel()
            t3 = threading.Timer(0.1,resendPackets)
            t3.start()           
        elif (util.nextseqnum < util.base + N and util.nextseqnum!=numOfPackets):
            p = packetList[util.nextseqnum]
            util.sendP(sendSocket, p, netAddr,netPort)
            #print("util.nextseqnum:" + str(util.nextseqnum))
            #print("numofPackets:" + str(numOfPackets))
            #print("base:"+str(util.base))
            #print("packet seq num:" + str(p.seq_num)+"\n")
            #TODO: start timer
            if (util.base==util.nextseqnum):                
                t3.cancel()
                t3 = threading.Timer(0.1,resendPackets)
                t3.start()
            util.nextseqnum += 1
            
    #send eotpacket 
    
    print("send_data done!")
                

#logName = "seqnum.log"


def listen_ack():
    #thread for listening ack
    print("thread listen_ack started\n")
    ackSocket = socket(AF_INET, SOCK_DGRAM)
    ackSocket.bind(("", senderPort))

    global t3
    acknum =""
    while (util.eotReceived!=True):
        message, addr = ackSocket.recvfrom(512)
        p = packet.parse_udp_data(message)

        util.base = p.seq_num + 1
        
        
        #log
        
        acknum += str(p.seq_num)+"\n"
        print("ack:" + str(p.seq_num)) #should we log eot???
        print("numPacket:" + str(numOfPackets))

        #start 
        if(util.base==util.nextseqnum):
            t3.cancel()
            #print("base=next");
        else:
            t3.cancel()
            t3 = threading.Timer(0.1,resendPackets)
            t3.start()
           # print("else")
        
        if (p.type==2):
            util.eotReceived = True
            #print("eotReceived:" + str(util.eotReceived))
            
    f = open("ack.log",'w')
    f.write(acknum)  
    f.close()
    
t1 = threading.Thread(target=listen_ack, name='t1') 
t2 = threading.Thread(target=send_data, name='t2')
t3 = threading.Timer(0.1,resendPackets)
t1.start() 
t2.start()  
    

f = open("myoutput.txt",'w')
i = 0
for p in packetList:
    
packetList.append(p)
