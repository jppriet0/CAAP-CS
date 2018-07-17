def sigma():
	summation = 0
	input("How many numbers are you going to add? ")
	E_list = eval(input("Okay. Now, please provide the numbers to add separated by commas. e.g. 1,2,3: "))
	for i in E_list:
		summation += i
	print("The total is: ", summation)
	returnE = input("Do you want to do another summation? (yes/no) ")
	if (returnE == "yes"):
		sigma()
	else: input("Press ENTER to return to the main screen")
