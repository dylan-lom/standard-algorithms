# Std. Algorithms, 4. Finding a minimum value in an array 

def FindMIN(Array, NumElementsInArray):
	Min = Array[0]
	MinIndex = 0
	for i in range(NumElementsInArray):
		if Array[i] < Min:
			Min = Array[i]
			MinIndex = i
	print("The lowest value in %d at position %d" % (Min, MinIndex))