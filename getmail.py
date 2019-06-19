#!/usr/bin/python

import sys
import re

file = open(sys.argv[1], "r")

fname = ""
lname = ""

def returnformat(fname, lname):
	format = sys.argv[2]
	format = re.split(r"[<>]", format)
	if format[1] == "fn":
		email = fname + format[2] + lname + format[4]
		return email
	if format[1] == "ln":
		email = lname + format[2] + fname + format[4]
		return email

for line in file:
	splitline = line.split(" ")
	if len(splitline) > 2:
		if splitline[2] == "-":
			fname = splitline[0]
			lname = splitline[1]
			email = returnformat(fname, lname)
			print(email)
			

      
