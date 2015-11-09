import Assignment3

def getAbbrev(stateName):
	for abbrev,name in Assignment3.myDict.items():
		if stateName == name:
			print abbrev