from socket import *
import sys
import threading
from packet import *
import time
import util

start = time.time()

N = 10
numOfPackets = 0
lock = threading.Lock()

if (len(sys.argv)>4):
    string = sys.argv[1]
    netAddr = string
    
    #get netPort
    string = sys.argv[2]
    if (string.isdigit()):
        netPort = int(string)    

    #get senderPort
    string = sys.argv[3]
    if (string.isdigit()):
        senderPort = int(string)
        
    #get fileName 
    fileName = sys.argv[4]
    
else:
    print ("Wrong number of parameters given\n")
    #exit()


packetList = [] #array of packets with data
f = open(fileName, 'r')
data = f.read(500)

#read data from the file and separate them into packets of 5oo bytes
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
f.close()

#add eot to the file
p = packet.create_eot(seqnum)
packetList.append(p)


logseq_num = ""

#resend packets upon timeout
def resendPackets():    
    while (util.eotReceived==False):
        global t3
        global logseq_num
        #restart timer 
        t3.cancel()
        t3 = threading.Timer(0.1,resendPackets)
        t3.start()

        
        sendSocket = socket(AF_INET, SOCK_DGRAM)
        with lock:
            #send packets GBN 
            count = util.base
            num = util.nextseqnum
            while (count<num):                
                p = packetList[count]
                util.sendP(sendSocket,p,netAddr,netPort)
                logseq_num += str(p.seq_num)+ "\n"                
                count+=1
            


def send_data():
    global t3
    global logseq_num
    #UDP socket to send data
    sendSocket = socket(AF_INET, SOCK_DGRAM)
    #log seqnum.log
    while (util.eotReceived==False):
        with lock:
            b = util.base
            n = util.nextseqnum
        #if there are still room, send next seqnum packet 
        if (n < b + N):
            if (n<=numOfPackets):
                p = packetList[n]
                logseq_num += str(p.seq_num)+ "\n"
                util.sendP(sendSocket, p, netAddr,netPort)
                if (b==n):
                    #start timer 
                    t3.cancel()
                    t3 = threading.Timer(0.1,resendPackets)
                    t3.start()
                util.nextseqnum += 1
    #print("send_data done!")



#thread for listening for ack
                
def listen_ack():
    #print("thread listen_ack started\n")
    ackSocket = socket(AF_INET, SOCK_DGRAM)
    ackSocket.bind(("", senderPort))
    global t3
    acknum =""

    while (util.eotReceived==False):
        message, addr = ackSocket.recvfrom(512)
        pp = packet.parse_udp_data(message)

        with lock:
            # update base number with received ack 
            multiplier = util.base // 32            
            if (pp.seq_num+ 32*multiplier<util.nextseqnum):
                util.base = pp.seq_num+ 32*multiplier + 1

            #log ack        
            acknum += str(pp.seq_num)+"\n"
            
            if(util.base==util.nextseqnum):
                t3.cancel()
            else:
                t3.cancel()
                t3 = threading.Timer(0.1,resendPackets)
                t3.start()

            if (pp.type==2):
                util.eotReceived = True
                

    #write ack file
    f = open("ack.log",'w')
    f.write(acknum)  
    f.close()

    #write seqnum log file
    f = open("seqnum.log",'w')
    f.write(logseq_num)
    f.close()
    end = time.time()
    
    
    f = open("time.log",'a')
    f.write(str(end-start))
    f.close()

t1 = threading.Thread(target=listen_ack, name='t1') 
t2 = threading.Thread(target=send_data, name='t2')
t3 = threading.Timer(0.1,resendPackets)
t1.start() 
t2.start()




