from threading import Thread

import socket

from time import sleep
from time import time

UDP_IP = "172.20.10.2"
UDP_PORT = 10000

fd = open("working.log", "w+")

def gps():
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
	sock.bind((UDP_IP, UDP_PORT))
	while True:
		data = sock.recvfrom(1024)
		fd.write(f"{time()} {data[0].decode('ASCII').strip()}\n")
		fd.flush()
		sleep(4)

import subprocess

def icmp():
	while True:
		rtt = subprocess.check_output(["bash", "ping-host.sh"])
		fd.write(f"{time()} {rtt.decode('ASCII').strip()}\n")
		fd.flush()
		sleep(4)

t1 = Thread(target=gps, args=(), daemon=True)
t1.start()

t2 = Thread(target=icmp, args=(), daemon=True)
t2.start()

while True:
	sleep(10)
