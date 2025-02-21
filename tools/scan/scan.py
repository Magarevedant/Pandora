
from queue import Queue
import socket
import threading

target = input("Enter the target: ")
queue = Queue()
open_ports = []


def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False

def get_ports(mode):
    if mode == 1:
        for port in range(1, 1024):
            queue.put(port)
    elif mode == 2:
        for port in range(1, 49152):
            queue.put(port)
    elif mode == 3:
        ports = [20, 21, 22, 23, 25, 53, 80, 110, 443]
        for port in ports:
            queue.put(port)
    elif mode == 4:
        ports = input("Enter your ports (seperate by blank):")
        ports = ports.split()
        ports = list(map(int, ports))
        for port in ports:
            queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("Port {} is open!".format(port))
            open_ports.append(port)

def run_scanner(threads, mode):

    get_ports(mode)

    thread_list = []

    for t in range(threads):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

    print("Open ports are:", open_ports)
    app()
    
print("""
# Please the mode of scaning the ports
[1] 1 - 1024
[2] 1 - 49152
[3] 20,21,22,23,25,53,80,110,443
[4] custom
[5] Exit
""")

def app():
	ch = int(input("Choice: "))
	if ch == 1:
		run_scanner(100, 1)
	elif ch == 2:
		run_scanner(100, 2)
	elif ch == 3:
		run_scanner(100, 3)
	elif ch == 4:
		run_scanner(100, 4)
	elif ch == 5:
		exit()
	else:
		pass
	app()
	
app()

  
