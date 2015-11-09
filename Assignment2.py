def sortcat(num, *therest):
	myList = list(therest)

	myString = ""
	count = 0
	while count < num:
		nextString = max(myList, key=len)
		myString += nextString
		myList.remove(nextString)
		count += 1
	print myString

sortcat(2, 'bc', 'c', 'abc')



