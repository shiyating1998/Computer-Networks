#PART C)
##i.	I think the controller has set-up to self-learn the rules on the switches. Whenever a request that is has not seen (not cached in the routing table), then it will self-learn the rules. It "installs" flows as ping requests happen. 
DEBUG:core:POX 0.3.0 (dart) going up...
DEBUG:core:Running on CPython (2.7.6/Oct 26 2016 20:30:19)
DEBUG:core:Platform is Linux-4.2.0-27-generic-x86_64-with-Ubuntu-14.04-trusty
INFO:core:POX 0.3.0 (dart) is up.
DEBUG:openflow.of_01:Listening on 0.0.0.0:6633
INFO:openflow.of_01:[00-00-00-00-00-07 5] connected
DEBUG:forwarding.l2_learning:Connection [00-00-00-00-00-07 5]
INFO:openflow.of_01:[00-00-00-00-00-02 6] connected
DEBUG:forwarding.l2_learning:Connection [00-00-00-00-00-02 6]
INFO:openflow.of_01:[00-00-00-00-00-03 3] connected
DEBUG:forwarding.l2_learning:Connection [00-00-00-00-00-03 3]
INFO:openflow.of_01:[00-00-00-00-00-01 8] connected
DEBUG:forwarding.l2_learning:Connection [00-00-00-00-00-01 8]
INFO:openflow.of_01:[00-00-00-00-00-06 7] connected
DEBUG:forwarding.l2_learning:Connection [00-00-00-00-00-06 7]
INFO:openflow.of_01:[00-00-00-00-00-04 2] connected
DEBUG:forwarding.l2_learning:Connection [00-00-00-00-00-04 2]
INFO:openflow.of_01:[00-00-00-00-00-05 4] connected
DEBUG:forwarding.l2_learning:Connection [00-00-00-00-00-05 4]

DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:05.1 -> 00:00:00:00:00:01.3
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:05.1 -> 00:00:00:00:00:01.3
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:05.2 -> 00:00:00:00:00:01.1
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:05.3 -> 00:00:00:00:00:01.1
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:05.3 -> 00:00:00:00:00:01.1
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:01.1 -> 00:00:00:00:00:05.3
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:01.1 -> 00:00:00:00:00:05.3
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:01.1 -> 00:00:00:00:00:05.2
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:01.3 -> 00:00:00:00:00:05.1
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:01.3 -> 00:00:00:00:00:05.1
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:05.1 -> 00:00:00:00:00:01.3
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:05.1 -> 00:00:00:00:00:01.3
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:05.2 -> 00:00:00:00:00:01.1
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:05.3 -> 00:00:00:00:00:01.1
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:05.3 -> 00:00:00:00:00:01.1
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:05.1 -> 00:00:00:00:00:01.3
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:05.1 -> 00:00:00:00:00:01.3
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:05.2 -> 00:00:00:00:00:01.1
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:05.3 -> 00:00:00:00:00:01.1
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:05.3 -> 00:00:00:00:00:01.1
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:01.1 -> 00:00:00:00:00:05.3
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:01.1 -> 00:00:00:00:00:05.3
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:01.1 -> 00:00:00:00:00:05.2
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:01.3 -> 00:00:00:00:00:05.1
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:01.3 -> 00:00:00:00:00:05.1
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:05.1 -> 00:00:00:00:00:01.3
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:05.1 -> 00:00:00:00:00:01.3
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:05.2 -> 00:00:00:00:00:01.1
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:05.3 -> 00:00:00:00:00:01.1
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:05.3 -> 00:00:00:00:00:01.1
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:01.1 -> 00:00:00:00:00:05.3
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:01.1 -> 00:00:00:00:00:05.3
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:01.1 -> 00:00:00:00:00:05.2
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:01.3 -> 00:00:00:00:00:05.1
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:01.3 -> 00:00:00:00:00:05.1

##ii. 
64 bytes from 10.0.0.5: icmp_seq=1 ttl=64 time=44.1 ms
64 bytes from 10.0.0.5: icmp_seq=2 ttl=64 time=0.945 ms
64 bytes from 10.0.0.5: icmp_seq=3 ttl=64 time=0.072 ms
64 bytes from 10.0.0.5: icmp_seq=4 ttl=64 time=0.051 ms
64 bytes from 10.0.0.5: icmp_seq=5 ttl=64 time=0.062 ms
64 bytes from 10.0.0.5: icmp_seq=6 ttl=64 time=0.077 ms
64 bytes from 10.0.0.5: icmp_seq=7 ttl=64 time=1.20 ms
64 bytes from 10.0.0.5: icmp_seq=8 ttl=64 time=0.095 ms
64 bytes from 10.0.0.5: icmp_seq=9 ttl=64 time=0.070 ms
64 bytes from 10.0.0.5: icmp_seq=10 ttl=64 time=0.084 ms

The first ping message are different with the subsequent ones because the first ping message, the switches have not yet learned the rules about which switches to forward. They have not yet set up their routing table. After the first ping message, the routes have been set up, so it becomes faster.


##iii.
###s1
cookie=0x0, duration=2.658s, table=0, n_packets=1, n_bytes=98, idle_timeout=10, hard_timeout=30, idle_age=2, priority=65535,icmp,in_port=2,vlan_tci=0x0000,dl_src=00:00:00:00:00:05,dl_dst=00:00:00:00:00:01,nw_src=10.0.0.5,nw_dst=10.0.0.1,nw_tos=0,icmp_type=0,icmp_code=0 actions=output:1
 cookie=0x0, duration=2.671s, table=0, n_packets=1, n_bytes=98, idle_timeout=10, hard_timeout=30, idle_age=2, priority=65535,icmp,in_port=1,vlan_tci=0x0000,dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:05,nw_src=10.0.0.1,nw_dst=10.0.0.5,nw_tos=0,icmp_type=8,icmp_code=0 actions=output:2


###s2
 cookie=0x0, duration=0.746s, table=0, n_packets=1, n_bytes=42, idle_timeout=10, hard_timeout=30, idle_age=0, priority=65535,arp,in_port=3,vlan_tci=0x0000,dl_src=00:00:00:00:00:05,dl_dst=00:00:00:00:00:01,arp_spa=10.0.0.5,arp_tpa=10.0.0.1,arp_op=1 actions=output:1
 cookie=0x0, duration=0.741s, table=0, n_packets=1, n_bytes=42, idle_timeout=10, hard_timeout=30, idle_age=0, priority=65535,arp,in_port=1,vlan_tci=0x0000,dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:05,arp_spa=10.0.0.1,arp_tpa=10.0.0.5,arp_op=2 actions=output:3
 cookie=0x0, duration=5.812s, table=0, n_packets=2, n_bytes=196, idle_timeout=10, hard_timeout=30, idle_age=4, priority=65535,icmp,in_port=1,vlan_tci=0x0000,dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:05,nw_src=10.0.0.1,nw_dst=10.0.0.5,nw_tos=0,icmp_type=8,icmp_code=0 actions=output:3
 cookie=0x0, duration=5.798s, table=0, n_packets=2, n_bytes=196, idle_timeout=10, hard_timeout=30, idle_age=4, priority=65535,icmp,in_port=3,vlan_tci=0x0000,dl_src=00:00:00:00:00:05,dl_dst=00:00:00:00:00:01,nw_src=10.0.0.5,nw_dst=10.0.0.1,nw_tos=0,icmp_type=0,icmp_code=0 actions=output:


###s3
 cookie=0x0, duration=7.856s, table=0, n_packets=4, n_bytes=392, idle_timeout=10, hard_timeout=30, idle_age=4, priority=65535,icmp,in_port=1,vlan_tci=0x0000,dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:05,nw_src=10.0.0.1,nw_dst=10.0.0.5,nw_tos=0,icmp_type=8,icmp_code=0 actions=output:3
 cookie=0x0, duration=7.833s, table=0, n_packets=4, n_bytes=392, idle_timeout=10, hard_timeout=30, idle_age=4, priority=65535,icmp,in_port=3,vlan_tci=0x0000,dl_src=00:00:00:00:00:05,dl_dst=00:00:00:00:00:01,nw_src=10.0.0.5,nw_dst=10.0.0.1,nw_tos=0,icmp_type=0,icmp_code=0 actions=output:1

###s4 
none

###s5
 cookie=0x0, duration=6.772s, table=0, n_packets=3, n_bytes=294, idle_timeout=10, hard_timeout=30, idle_age=4, priority=65535,icmp,in_port=3,vlan_tci=0x0000,dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:05,nw_src=10.0.0.1,nw_dst=10.0.0.5,nw_tos=0,icmp_type=8,icmp_code=0 actions=output:1
 cookie=0x0, duration=6.765s, table=0, n_packets=3, n_bytes=294, idle_timeout=10, hard_timeout=30, idle_age=4, priority=65535,icmp,in_port=1,vlan_tci=0x0000,dl_src=00:00:00:00:00:05,dl_dst=00:00:00:00:00:01,nw_src=10.0.0.5,nw_dst=10.0.0.1,nw_tos=0,icmp_type=0,icmp_code=0 actions=output:3

###s6
 cookie=0x0, duration=4.957s, table=0, n_packets=2, n_bytes=196, idle_timeout=10, hard_timeout=30, idle_age=3, priority=65535,icmp,in_port=3,vlan_tci=0x0000,dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:05,nw_src=10.0.0.1,nw_dst=10.0.0.5,nw_tos=0,icmp_type=8,icmp_code=0 actions=output:1
 cookie=0x0, duration=4.955s, table=0, n_packets=2, n_bytes=196, idle_timeout=10, hard_timeout=30, idle_age=3, priority=65535,icmp,in_port=1,vlan_tci=0x0000,dl_src=00:00:00:00:00:05,dl_dst=00:00:00:00:00:01,nw_src=10.0.0.5,nw_dst=10.0.0.1,nw_tos=0,icmp_type=0,icmp_code=0 actions=output:3
###s7
none

These flow rules are different than what I defined in part A, as they do not specify MAC address numbers and they have a time-out that it will expire. 
Collectively, it does similar things as what we route from h1 to h6, they set each switches, s3 to s2, s2 to s1, s1 to s5, and s5 to s6 to route from h1 to h6. And we can see from the dump-flows that s4 and s7 have no entries. Since they are needed in transfering packets from h1 to h6. 