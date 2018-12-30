# Std. Alogirithms, 1. Load an array and print out it's contents

def LoadArray(Array):
	i = 0 #index -- indexing from zero nicely means that the sentinal value doesn't affect the total :)
	DataValue = Array[i]
	while DataValue != "xxx":
		i += 1
		DataValue = Array[i]
	NumElements = i #stooopid
	print("There are %d items loaded into the array" % (NumElements))
	return NumElements
	
def PrintArray(Array, NumElements):
	# realistic approach
	#for i in Array:
	#	print(i)
	
	# documented method
	for i in range(NumElements):
		print(Array[i])
		
MyArray = ["hello", "world", "123", "xxx"]
NumElements = LoadArray(MyArray)
PrintArray(MyArray, NumElements)