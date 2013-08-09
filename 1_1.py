#!/usr/bin/python

string = raw_input("Please enter a string that is at least 3 characters long: ")

while len(string) < 3:
  string = raw_input("Sorry, the string was shorter than 3 characters, please try again: ")

if len(string) >= 3:
  print "Third char in string:",string[2]
  print "Last char in string :",string[-1]

