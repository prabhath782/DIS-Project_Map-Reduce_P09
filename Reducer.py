#!/usr/bin python
import sys

reduceIn = open("mapOut.txt", "r")
s = open("sorted.txt","r","w")
reduceOut = open("reduceOut.txt", "w")



lines = reduceIn.readlines()
lines.sort()
for line in lines:
	s.write(line)

total = 0
oldKey = None
count = 0

for line in lines:
	data: line.strip().split('\t')
	if len(data)!= 2:
		continue
	pAge, pMedi = data
	
	
    if oldKey and oldKey != pAge:        
        reduceOut.write("{0}\t{1}\n".format(oldKey, total))
        oldKey = pAge;
        total = 0
	if pMedi.equals("Continuing"):
		total += 1
	
    oldKey = pAge            
    
	
	if oldKey != None: 
		reduceOut.write("{0}\t{1}\n".format(oldKey, total))

reduceIn.close()
s.close() 
reduceOut.close() 
