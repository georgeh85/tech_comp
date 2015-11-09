myDict = {}
statesList = open('states.txt', 'r+')
for line in statesList:
	a,b = line.strip().split(',')
	myDict[b.strip()] = a.strip()

statesList.close()

def getState(abbrev):
	for abbreviation in myDict.keys():
		if abbrev == abbreviation:
			print myDict[abbreviation]

