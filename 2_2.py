#!/usr/bin/python

import urllib2
import sys

url = 'http://www.rackspace.co.uk'
try:
  url_content = urllib2.urlopen(url)
except urllib2.URLError:
  print "Failed to open %s. Please check the spelling." % url
  sys.exit(1)

for i in xrange(9):
  print url_content.readline().rstrip()

