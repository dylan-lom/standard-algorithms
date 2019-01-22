# Std. Algorithms, 5. Extracting data from a string

def FindDaysandMonths(DateString):
	StartDays, StartMonths, StartYears= 0, 2, 4 # DD/MM/YY format
	# Day = DateString[StartDays:StartMonths]
	# Month = DateString[StartMonths:StartYears]
	
	# specification approach
	Day = DateString[StartDays] + DateString[StartDays+1]
	Month = DateString[StartMonths] + DateString[StartMonths+1]
	print("The month is %s, and the day of the month is %s" % (Month, Day))
	
FindDaysandMonths("311218")