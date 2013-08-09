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

print "The following servers exist in your account:"
for server in cs.servers.list():
  print "\tServer Name:", server.name
