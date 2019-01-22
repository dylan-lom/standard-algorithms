def DisplayFileContents():
	with open("FriendsData", "r") as FriendsData: #priming read, not really sure about this one...
	
		line = FriendsData.readline()
		while line != "xxx":
			print(line, end='')
			line = FriendsData.readline()

DisplayFileContents()
