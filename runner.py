from os import listdir
from os.path import isfile, join
import glob
import os
import sys
import time

import argparse

start_time = time.time()
print(f"Start time of runner.py: {start_time}")

text = "=======Splitting======="

parser = argparse.ArgumentParser(description = text)  
#parser.parse_args()  

parser.add_argument("-i", "--input", help="Input directory")
parser.add_argument("-o", "--output", help="Output directory")
parser.add_argument("-t", "--tper", help="Minimum length")
parser.add_argument("-mset", "--mset", help="mset model")

# read arguments from the command line
args = parser.parse_args()
output = "Output"
if args.output:
	output = args.output
folder = args.input

pattern = os.path.join(folder, '*')

filepaths = glob.glob(pattern) 
for filepath in filepaths:
    if os.path.isfile(filepath):
        cmd = "python2.7 mPartition.py -f \"{0}\" -o \"{1}\"".format(filepath, output)
        if args.tper:
            cmd += " -t {0}".format(args.tper)
        if args.mset:
            cmd += " -mset {0}".format(args.mset)
        os.system(cmd)

end_time = time.time()
print(f"Finish time of runner.py: {end_time}")

execution_time = end_time - start_time
print(f"Execution time of runner.py: {execution_time}")