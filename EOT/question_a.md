#PART A) Hands on OpenFlow
##vi. 
h1 ping h0 works now. The flow entries that I entered added flow between for switches s0 and s1. 
In s0, port number:6634, it specified the flow for packets received from source:10.0.1.2(h1), that came in from port 2, and destined:10.0.0.2(h2), then it will do the following action, go through this link: 0A:00:00:01:00:01, it will output to the link:0A:00:00:02:00:00 and output it through port 1.
It does the similar thing for packets received from h2 and destined to h1.
Similarly, in s1, port number:6635, it also sets flows for packets from h1 to h2 and from h2 to h1 with specific MAC address and in_port and output. 
##vii. 
###h2<->h4
####command on s2: 
ovs-vsctl set bridge s2 protocols=OpenFlow13
ovs-ofctl -O OpenFlow13 add-flow tcp:127.0.0.1:6636 in_port=1,ip,nw_src=10.0.2.2,nw_dst=10.0.4.2,actions=mod_dl_src:0A:00:0D:01:00:04,mod_dl_dst:0A:00:0D:FE:00:02,output=4
ovs-ofctl -O OpenFlow13 add-flow tcp:127.0.0.1:6636 in_port=4,ip,nw_src=10.0.4.2,nw_dst=10.0.2.2,actions=mod_dl_src:0A:00:02:01:00:01,mod_dl_dst:0A:00:02:02:00:00,output=1
####command on s3: 
ovs-vsctl set bridge s3 protocols=OpenFlow13
ovs-ofctl -O OpenFlow13 add-flow tcp:127.0.0.1:6637 in_port=2,ip,nw_src=10.0.2.2,nw_dst=10.0.4.2,actions=mod_dl_src:0A:00:0E:01:00:03,mod_dl_dst:0A:00:0E:FE:00:02,output=3
ovs-ofctl -O OpenFlow13 add-flow tcp:127.0.0.1:6637 in_port=3,ip,nw_src=10.0.4.2,nw_dst=10.0.2.2,actions=mod_dl_src:0A:00:0D:FE:00:02,mod_dl_dst:0A:00:0D:01:00:04,output=2
####command on s4: 
ovs-vsctl set bridge s4 protocols=OpenFlow13
ovs-ofctl -O OpenFlow13 add-flow tcp:127.0.0.1:6638 in_port=2,ip,nw_src=10.0.2.2,nw_dst=10.0.4.2,actions=mod_dl_src:0A:00:04:01:00:01,mod_dl_dst:0A:00:04:02:00:00,output=1
ovs-ofctl -O OpenFlow13 add-flow tcp:127.0.0.1:6638 in_port=1,ip,nw_src=10.0.4.2,nw_dst=10.0.2.2,actions=mod_dl_src:0A:00:0E:FE:00:02,mod_dl_dst:0A:00:0E:01:00:03,output=2

###h1<->h6
####command on s1: 
ovs-vsctl set bridge s1 protocols=OpenFlow13
ovs-ofctl -O OpenFlow13 add-flow tcp:127.0.0.1:6635 in_port=1,ip,nw_src=10.0.1.2,nw_dst=10.0.6.2,actions=mod_dl_src:0A:00:0C:01:00:03,mod_dl_dst:0A:00:0D:01:00:04,output=3
ovs-ofctl -O OpenFlow13 add-flow tcp:127.0.0.1:6635 in_port=3,ip,nw_src=10.0.6.2,nw_dst=10.0.1.2,actions=mod_dl_src:0A:00:01:01:00:01,mod_dl_dst:0A:00:01:02:00:00,output=1
####command on s2:
ovs-vsctl set bridge s2 protocols=OpenFlow13
ovs-ofctl -O OpenFlow13 add-flow tcp:127.0.0.1:6636 in_port=3,ip,nw_src=10.0.1.2,nw_dst=10.0.6.2,actions=mod_dl_src:0A:00:0D:01:00:04,mod_dl_dst:0A:00:0D:FE:00:02,output=4
ovs-ofctl -O OpenFlow13 add-flow tcp:127.0.0.1:6636 in_port=4,ip,nw_src=10.0.6.2,nw_dst=10.0.1.2,actions=mod_dl_src:0A:00:0C:FE:00:03,mod_dl_dst:0A:00:0C:01:00:03,output=3
####command on s3:
ovs-vsctl set bridge s3 protocols=OpenFlow13
ovs-ofctl -O OpenFlow13 add-flow tcp:127.0.0.1:6637 in_port=2,ip,nw_src=10.0.1.2,nw_dst=10.0.6.2,actions=mod_dl_src:0A:00:0F:01:00:04,mod_dl_dst:0A:00:0F:FE:00:02,output=4
ovs-ofctl -O OpenFlow13 add-flow tcp:127.0.0.1:6637 in_port=4,ip,nw_src=10.0.6.2,nw_dst=10.0.1.2,actions=mod_dl_src:0A:00:0D:FE:00:02,mod_dl_dst:0A:00:0D:01:00:04,output=2
####command on s6:
ovs-vsctl set bridge s6 protocols=OpenFlow13
ovs-ofctl -O OpenFlow13 add-flow tcp:127.0.0.1:6640 in_port=2,ip,nw_src=10.0.1.2,nw_dst=10.0.6.2,actions=mod_dl_src:0A:00:06:01:00:01,mod_dl_dst:0A:00:06:02:00:00,output=1
ovs-ofctl -O OpenFlow13 add-flow tcp:127.0.0.1:6640 in_port=1,ip,nw_src=10.0.6.2,nw_dst=10.0.1.2,actions=mod_dl_src:0A:00:0F:FE:00:02,mod_dl_dst:0A:00:0F:01:00:04,output=2

###h0<->h3
#####command on s0:
ovs-vsctl set bridge s0 protocols=OpenFlow13
ovs-ofctl -O OpenFlow13 add-flow tcp:127.0.0.1:6634 in_port=1,ip,nw_src=10.0.0.2,nw_dst=10.0.3.2,actions=mod_dl_src:0A:00:0B:01:00:03,mod_dl_dst:0A:00:0B:FE:00:02,output=3
ovs-ofctl -O OpenFlow13 add-flow tcp:127.0.0.1:6634 in_port=3,ip,nw_src=10.0.3.2,nw_dst=10.0.0.2,actions=mod_dl_src:0A:00:00:01:00:01,mod_dl_dst:0A:00:00:02:00:00,output=1
####command on s2:
ovs-vsctl set bridge s2 protocols=OpenFlow13
ovs-ofctl -O OpenFlow13 add-flow tcp:127.0.0.1:6636 in_port=2,ip,nw_src=10.0.0.2,nw_dst=10.0.3.2,actions=mod_dl_src:0A:00:0D:01:00:04,mod_dl_dst:0A:00:0D:FE:00:02,output=4
ovs-ofctl -O OpenFlow13 add-flow tcp:127.0.0.1:6636 in_port=4,ip,nw_src=10.0.3.2,nw_dst=10.0.0.2,actions=mod_dl_src:0A:00:0B:FE:00:02,mod_dl_dst:0A:00:0B:01:00:03,output=2
####command on s3:
ovs-vsctl set bridge s3 protocols=OpenFlow13
ovs-ofctl -O OpenFlow13 add-flow tcp:127.0.0.1:6637 in_port=2,ip,nw_src=10.0.0.2,nw_dst=10.0.3.2,actions=mod_dl_src:0A:00:03:01:00:01,mod_dl_dst:0A:00:03:02:00:00,output=1
ovs-ofctl -O OpenFlow13 add-flow tcp:127.0.0.1:6637 in_port=1,ip,nw_src=10.0.3.2,nw_dst=10.0.0.2,actions=mod_dl_src:0A:00:0D:FE:00:02,mod_dl_dst:0A:00:0D:01:00:04,output=2

