def convertA():
	direction = input("For P->LY type 'parsec', for LY->P type 'light year': ")
	if (direction == "parsec"):
		valueP = eval(input("Input the temp. value in Parsecs: "))
		operationP = 3.26156*valueP
		print("That temperature is equivalent to " , operationP , "Light Years.")
		returnP = input("Do you want to do another conversion? (yes/no) ")
		if (returnP == "yes"):
			convertA()
		else: input("Press ENTER to return to the main screen")
	elif (direction == "light year"):
		valueL = eval(input("Input the temp. value in Light Years: "))
		operationL = valueL/3.26156
		print ("That temperature is equivalent to" , operationL , "Parsecs.")
		returnL = input("Do you want to do another conversion? (yes/no) ")
		if (returnL == "yes"):
			convertA()
		else: input("Press ENTER to return to the main screen")
		