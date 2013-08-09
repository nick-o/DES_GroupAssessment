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

cs = pyrax.cloudservers
image = [img for img in cs.images.list()if "CentOS 6.4" in img.name][0]
flavor = [flavor for flavor in cs.flavors.list()if flavor.ram == 512][0]

server = cs.servers.create(os.uname()[1], image.id, flavor.id)

print "Your Cloud Server has been created successfully!"
print "Please find its details below:"
print "\tName:",server.name
print "\tID:",server.id
print "\tImage name:",image.name
print "\tFlavor:",flavor.name
