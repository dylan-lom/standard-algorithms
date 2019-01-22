def AddNewRecords():
	with open("FriendsData", "a") as fd:
		print("Please enter additional details.")
		print("When no more records are to be added, enter 'xxx' for first name")

		fname = input("First Name: ")
		while fname != "xxx":
			sname = input("Second Name: ")
			emailaddr = input("Email Address: ")
			mobile = input("Mobile Number: ")
			fd.write(fname + ", " + sname + ", " + emailaddr + ", " + mobile + "\n")
			fname = input("First Name: ")
		fd.write("xxx")

AddNewRecords()
