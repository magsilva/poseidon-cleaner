#!/usr/bin/python

import os
import re
import sys

def detect_poseidon_signature():
	return true

def prepare_input_file(filename):
#	if not os.access(filename, F_OK | R_OK):
#		return False
	return True

def prepare_output_file(filename):
#	if not os.access(filename, F_OK | W_OK):
#		return False
	return True

def remove_box1(text):
	pattern = re.compile(r"""^0\.0 0\.0 0\.0 RG$
^\[ 1\.0 0\.0 0\.0 1\.0 0\.0 0\.0 \] defaultmatrix matrix concatmatrix setmatrix$
^1\.0 w$
^2 J$
^0 j$
^10\.0 M$
^\[ \] 0\.0 d$
^1\.0 1\.0 1\.0 RG$
^0\.0 0\.0 \d+\.0 \d+\.0 rf$
^0\.0 0\.0 0\.0 RG$
^q$
^0 0 \d+ \d+ rc$
^q$""", re.M )

	if pattern.search(text) == None:
		return False
	
	text = pattern.sub('', text)
	return text
	

def remove_box2(text):
	pattern = re.compile(r"""^f$
^0\.501961 0\.501961 0\.501961 RG$
^newpath$
""", re.M )

	if pattern.search(text) == None:
		return False
	
	text = pattern.sub('', text)
	return text

def remove_box3(text):
	pattern = re.compile(r"""^0\.0 12\.0 moveto$
^q 1 -1 scale$
^/Helvetica findfont 12.0 scalefont setfont$
^\(Created with Poseidon for UML Community Edition\. Not for Commercial Use\.\) show$
^Q$
^\[ 1\.0 0\.0 0\.0 1\.0 -?\d+\.0 \d+\.0 \] defaultmatrix matrix concatmatrix setmatrix$
^\[ 1\.0 0\.0 0\.0 1\.0 0\.0 0\.0 \] defaultmatrix matrix concatmatrix setmatrix$
^newpath$
^0\.0 0\.0 m$
^0\.0 \d+\.0 l$
^\d+\.0 \d+\.0 l$
^\d+\.0 0\.0 l$
^h$""", re.M)
	
	if pattern.search(text) == None:
		return False
	
	text = pattern.sub('', text)
	return text



def remove_label(text):
	pattern = re.compile(r"""^S$
^2 J$
^10\.0 M$
^\[ 1\.0 0\.0 0\.0 1\.0 \d\.\d \d\.\d \] concat$
^0\.0 11\.0 moveto$
^q 1 -1 scale$
^/SansSerif findfont 11.0 scalefont setfont$
^\(.*\) show$""" , re.M)

	if pattern.search(text) == None:
		return False
	
	text = pattern.sub('', text)
	return text
	


print "Checking if %s is an Poseidon generated encapsulated postscript..." % (sys.argv[1]),
if not prepare_input_file(sys.argv[1]):
	print "Err"
	exit
print "Ok"

print "Creating file %s to write the processed file..." % (sys.argv[2]),
if not prepare_output_file(sys.argv[2]):
	print "Err"
	exit
print "Ok"

source = open(sys.argv[1], "r")
dest = open(sys.argv[2], "w+")

image = source.read()
image = remove_box1(image)
image = remove_box2(image)
image = remove_box3(image)
image = remove_label(image)

dest.write(image)
