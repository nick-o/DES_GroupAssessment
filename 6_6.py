#!/usr/bin/python

# Echo server program
import socket
import sys

query_user = True
while query_user:
  try:
    number = int(raw_input("Please enter the port you want the echo server to listen on:"))
    if number < 1 or number > 65535:
      print "The port needs to be greater than 0 and lower than 65536"
    else:
      query_user = False
  except ValueError:
    print "You need to enter a valid Integer!!"


HOST = ''            
PORT = number
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
  s.bind((HOST, PORT))
except:
  print 'Can\'t bind port number %i. Exiting.' % number
  sys.exit(1)
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr
while 1:
    data = conn.recv(1024)
    if not data: break
    conn.send(data)
conn.close()

print 'Remote connectiong closed, Exiting!'
