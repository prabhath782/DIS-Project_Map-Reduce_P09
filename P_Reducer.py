import sys


continuingTotal = 0
reducedTotal = 0
oldKey = None


for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisvalue = data_mapped


    if oldKey and oldKey != thisKey:
       # print "\tAge group of people:", oldKey, "\tNumber of people who have medication type: Continuing", continuingTotal, "\tNumber of people who have medication type reduced", reducedTotal
	print oldKey, continuingTotal, reducedTotal
        oldKey = thisKey;
        continuingTotal = 0
	reducedTotal = 0

    oldKey = thisKey
    if thisvalue == 'continuing':
   	    continuingTotal += 1
    elif thisvalue == 'reduced':
        reducedTotal += 1

if oldKey != None:
    #print "\tAge group of people:", oldKey, "\tNumber of people who have medication type: Continuing", continuingTotal, "\tNumber of people who have medication type reduced", reducedTotal
	print oldKey, continuingTotal, reducedTotal
