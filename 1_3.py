#!/usr/bin/python
import sys

file = "./text.txt"

try:
  f = open(file,"r")
except IOError:
  print "Error, can\'t find %s. Please make sure it exists" % file
  sys.exit(1)


query_user = True
while query_user:
  try:
    number = int(raw_input("Please specify the number of the line you want to print from %s :" % file))
    query_user = False
  except ValueError:
    print "You need to enter a valid Integer!!"

i = 0
for i in xrange(number - 1):
  line = f.readline()
  if not line:
    print "Sorry, the file has less than %i lines in it" % number
    sys.exit(1)


print f.readline()
