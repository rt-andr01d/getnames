#!/usr/bin/python

import argparse
import sys
import re

###python getname.py -f file.txt -e <fn>.<ln>@email.com

parser = argparse.ArgumentParser(description='Create emails based on a google search result')
parser.add_argument('-f', '--file', help='Text file containing google search', required=True)
parser.add_argument('-e', '--emailformat', help='Format you would like the email in. e.g. <fn>.<ln>@gmail.com', required=True)
parser.add_argument('-o', '--outfile', help='File to write output to')
args = parser.parse_args()

if args.outfile:
	outfile = open(sys.argv[6], "w")

file = open(sys.argv[2], "r")

fname = ""
lname = ""

def returnformat(fname, lname):
	format = sys.argv[4]
	format = re.split(r"[<>]", format)
	if format[2] == ".":
		if format[1] == "fn":
			email = fname + format[2] + lname + format[4]
			return email
		if format[1] == "ln":
			email = lname + format[2] + fname + format[4]
			return email
	else:
		if format[1] == "fn":
			email = fname + lname + format[4]
			return email
		if format[1] == "ln":
			email = lname + fname + format[4]
			return email

for line in file:
	splitline = line.split(" ")
	if len(splitline) > 2:
		if splitline[2] == "-":
			fname = splitline[0]
			lname = splitline[1]
			email = returnformat(fname, lname)
			if args.outfile:
				outfile.write(email)
				outfile.write("\n")
			else:
				print(email)
			

      
