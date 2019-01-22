# Std. Algorithms, 2. Add the contents of an array of numbers

def SumArrayContents(Array, NumElements):
	total = 0
	for i in range(NumElements):
		total += Array[i]
	print("The sum of all of the elements in the array = %d" % (total))
	
def SumArrayContentsPreTest(Array): #unknown NumElements
	i = 0
	total = 0
	while Array[i] != 999: #where 999 is sentinal
		total += Array[i]
		i += 1
	print("There are %d elements" % (i))
	print("The sum of all of the elements in the array = %d" % (total))
