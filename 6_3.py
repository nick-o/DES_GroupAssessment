#!/usr/bin/python

import pyrax
import os
import sys

auth_file = "~/.pyrax/auth"

pyrax.set_setting('identity_type','rackspace')
pyrax.set_setting('region','LON')
try:
  pyrax.set_credential_file(os.path.expanduser(auth_file))
except pyrax.exceptions.FileNotFound:
  print "The auth file in %s does not exist. Please verify it is there." % auth_file
  sys.exit(1)
except pyrax.exceptions.AuthenticationFailed:
  print "Unable to authenticate with the credentials found in %s. Please verify that they are correct." % auth_file
  sys.exit(1)

cf = pyrax.cloudfiles

import urllib

#Unfortunately I could not find the actual logo but only something containing the logo
url = 'http://c3334822.r22.cf0.rackcdn.com/global_header.png'
resp = urllib.urlretrieve(url,'global_header.png')
for head in resp[1].headers:
  if head.split(":")[0] == "Content-Type":
    if not head.split(":")[1].lstrip().startswith('image'):
      print "The file at %s was not an image or could not be dowloaded. Aborting..." % url
      sys.exit(1)

container = cf.create_container('example')
pth = 'global_header.png'
chksum = pyrax.utils.get_checksum(pth)
obj = cf.upload_file("example", pth, etag=chksum)

temp_url =  obj.get_temp_url(300)
print "The Rackspace logo has been uploaded to Cloud Files successfully"
print "Temporary URL for the file (valid for 5min):", temp_url

