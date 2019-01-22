def CreateAFile():
	with open("FriendsData", "w") as FriendsData:
		for i in range(10):
			print("Please enter the details for the next person")
			fname = input("First Name: ")
			sname = input("Second Name: ")
			emailaddr = input("Email Address: ")
			mobile = input("Mobile Number: ")
			
			FriendsData.write(fname + ", " + sname + ", " + emailaddr + ", " + mobile + "\n")
		FriendsData.write("xxx") # the example sentinal stuff confuses me

CreateAFile()
