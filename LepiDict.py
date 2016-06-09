#!/usr/bin/env python

InFileName = "MM_Lepido_3_play.sbd"

InFile = open(InFileName, 'r')

for Line in InFile:
	Line = Line.split ()
	if Line[0] == '---':
		continue
	if len(Line) == 1:  
		print Line





