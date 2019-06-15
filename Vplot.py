import os
import pysam 
import sys
import re
import matplotlib.pyplot as plt
sam_file = open(sys.argv[1])
chromosome = sys.argv[2]
start = sys.argv[3]
end = sys.argv[4]
#input the path of the sam file at the command line
length = 0
midpoint = 0
for read in sam_file.fetch(chromosome, start, end):
     print(read)
for line in sam_file:
	if line.startswith("D"):
		split = line.split("\t")
		endposition = (split[7])
		startposition = (split[3])
		midpointnew= (float(endposition)+ float(startposition))/2
		midpoint = str(midpoint) + "," + str(midpointnew)
		newlength = abs(int(split[8]))
		length = str(length) + "," + str(newlength)
length = [ float(x) for x in length.split(',') ]
midpoint = [ float(x) for x in midpoint.split(',') ]
midpoint = midpoint[1:]
length = length[1:]
plt.scatter(midpoint,length, s = .1, alpha = .1)
plt.show()