# Std. Algorithms, 7. Deletion of a string from another string

def DeleteWordFromString(InitialString, StringToGo):
	LString = len(InitialString)
	LWord = len(StringToGo)
	i, Found = 0, False
	
	while i+LWord <= LString and not Found:
		CheckforWord = InitialString[i:i+LWord]
		#print(CheckforWord)
		if CheckforWord == StringToGo:
			FirstPart = InitialString[:i]
			SecondPart = InitialString[i+LWord:]
			NewString = FirstPart + SecondPart
			Found = True
		i+=1
		
	if not Found:
		print("The word could not be found in your string.")
	else:
		print("The new string is '%s'" % NewString)
		
DeleteWordFromString("you're brandons mom lol", "brandons ")