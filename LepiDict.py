#!/usr/bin/env python
from collections import defaultdict 
InFileName = "Lepi_Cell.txt"

InFile = open(InFileName, 'r')


counter=0 #counter for cell observations
mydict=defaultdict(list) 
for Line in InFile:
	if len(Line.split())==1:
		holder=str(counter)
		print (holder)
		print ('here'+Line)
		counter+=1
	else:
		mydict['cell-'+holder].append([Line.split()[1],Line.split()[2]])
		#print (Line)

print (mydict['cell-0'])

def distSquared(p0, p1):
   return (p0[0][0] - p1[0][0])**2 + (p0[1][1] - p1[1][1])**2
 
oInput = [[9.5, 7.5], [0.2, 19.1]]
print (distSquared(oInput,oInput))

for keys in mydict.keys():
	for pair in mydict[keys]:
		print (distSquared(pair)) #one give one pair


#def distance(points):
#    p0, p1 = points
 #   return math.sqrt((P0[1] - p1[1])**2 + (p0[2] - p1[2])**2)

  #	min_distance = distance(Line.split()[1],Line.split () [2])

#	for p0, p1 in itertools.combinations(Line.split, 2):
 #   min_distance = min(min_distance, distance(p0, p1))

