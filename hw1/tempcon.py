def convertT():
	direction = input("For C->F type 'celsius', for F->C type 'farenheit': ")
	if (direction == "celsius"):
		valueC = eval(input("Input the temp. value in Celsius: "))
		operationC = 1.8*valueC + 32
		print ("That temperature is equivalent to" , operationC , "Fahrenheit.")
		returnC = input("Do you want to do another conversion? (yes/no) ")
		if (returnC == "yes"):
			convertT()
		else: input("Press ENTER to return to the main screen")
	elif (direction == "farenheit"):
		valueF = eval(input("Input the temp. value in Farenheit: "))
		operationF = (valueF - 32) / 1.8
		print ("That temperature is equivalent to" , operationF , "Celsius.")
		returnF = input("Do you want to do another conversion? (yes/no) ")
		if (returnF == "yes"):
			convertT()
		else: input("Press ENTER to return to the main screen")
	else:
			print("Unit not accepted, try again.")
			convertT()
		
