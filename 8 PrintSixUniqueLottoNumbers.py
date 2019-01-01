# Std. Algorithms, 8. Generating a set of unique random numbers

from random import randint

def PrintSixUniqueLottoNumbers():
	Flag = [False] * 100
	
	for i in range(6):
		r = randint(1,99) #this is what they do.. i think.. this one's really confusing/bad
		while Flag[r]:
			r = randint(1,99)
			#print(r)
		Flag[r] = True #number found
		print("Your next number is %d" % r)
		
PrintSixUniqueLottoNumbers()