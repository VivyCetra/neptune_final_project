#!/usr/bin/env python

InFileName = "MM_Lepido_3_play.sbd"

InFile = open(InFileName, 'r')


counter=0
for Line in InFile:
	Mylist = []
	Line = Line.split ()
	if Line[0] == '---':
		continue
	if len(Line) == 1:  
		for i in range (int(Line[0]))
			mylist.append( [ Line [2],Line  [3] ] )


 


