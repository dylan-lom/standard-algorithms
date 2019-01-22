# Std. Algorithms, 3. Finding a maximum value in an array

def FindMAX(Array, NumElementsInArray):
	Max = Array[0]
	MaxIndex = 0
	for i in range(NumElementsInArray):
		if Array[i] > Max:
			Max = Array[i]
			MaxIndex = i
	
	print("The highest value is %d at %d" % (Max, MaxIndex))