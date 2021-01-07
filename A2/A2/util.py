eotReceived = False 

'''function to send packets'''
def sendP(socket, p, netAddr, netPort):
    UDPData = p.get_udp_data()
    socket.sendto(UDPData ,(netAddr,netPort))


'''for sender'''
base = 0
nextseqnum = 0


