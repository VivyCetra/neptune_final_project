#!/usr/bin/env python
from collections import defaultdict 
from scipy.spatial.distance import pdist
import numpy

InFileName = "Lepi_Cell.txt"

InFile = open(InFileName, 'r')


counter=0 #counter for cell observations
mydict=defaultdict(list) 
for Line in InFile:
	if len(Line.split())==1:
		holder=str(counter)
		print (holder)
		print ('cell_number'+Line)
		counter+=1

 
	else:
		mydict['cell-'+holder].append([Line.split()[1],Line.split()[2]])
		


for keys in mydict.keys():
	if len(mydict[keys]) == 1:
		continue
	result = numpy.array(mydict[keys])
	mindist = numpy.min(pdist(result))
	maxdist = numpy.max(pdist(result))

	print ('{}: min:{} max:{} ' .format(keys, mindist, maxdist))


