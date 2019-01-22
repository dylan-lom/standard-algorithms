# Std. Alogirithms, 6. Insertion of a string into another string

def InsertNewWordintoString(InitialString, NewWord):
	L = len(InitialString)
	Found = False
	i = 0
	while i <= L and not Found:
		if InitialString[i] == ";":
			FirstPart = InitialString[0:i]
			SecondPart = InitialString[i+1:L]
			NewString = FirstPart + NewWord + SecondPart
			Found = True
		i += 1
	if not Found:
		print("The delimiter, ';', could not be found in your string.")
	else:
		print("The new string is '%s'" % NewString)
		
InsertNewWordintoString("My name is ;, nice to meet you!", "hjegff")