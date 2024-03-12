#Author: Thulek@gmail.com
#Split an alignment into sub-alignments using a predefined partitioning scheme
 
from os import listdir
from os.path import isfile, join
import os
import sys
import platform
import subprocess
import time

import array as arr
import random

import argparse
parser = argparse.ArgumentParser() 

parser.add_argument("-f", "--filex", help="File")
parser.add_argument("-p", "--part", help="par file")
args = parser.parse_args()

parFile = args.part
filex = args.filex

def line_prepender(filename, line):
	with open(filename, 'r+') as f:
		content = f.read()
		f.seek(0, 0)
		f.write(line.rstrip('\r\n') + '\n' + content)


parF = open(parFile,"r")
for line in parF:
	if "=" in line:
		siteArr = line.split("=")[1].strip().replace(";","").replace(",","")
		#parname = line.split("=")[0].strip()
		parname = line.split("=")[0].strip("\tcharset ")

		parname.replace(" ","")
		siteList = siteArr.split(" ")
		if os.path.isfile(filex+str(parname)):
			os.system("rm "+filex+str(parname))
		par = open(filex+str(parname),"w")
		print(filex+str(parname) + "here")
		fil = open(filex,"r")
		noOfTax = 0
		for lx in fil:
			if noOfTax > 0:
				if " " in lx:
					seq1 = lx.split(" ",1)
					par.write(str(seq1[0].strip())+" ")
					seqContent = seq1[1].strip()
					for x in siteList:
						par.write(seqContent[int(x.strip())-1])
					par.write("\n")
				elif "\t" in lx:
					seq1 = lx.split("\t",1)
					par.write(str(seq1[0].strip())+" ")
					seqContent = seq1[1].strip()
					for x in siteList:
						par.write(seqContent[int(x.strip())-1])
					par.write("\n")
			noOfTax += 1
		fil.close()
		par.close()
		line_prepender(filex+str(parname), str(noOfTax-1)+" "+str(len(siteList)))
parF.close()
