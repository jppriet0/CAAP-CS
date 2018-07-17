def count():
	Dollars = (10000,5000,2000,1000,500,200,100,25,10,5,1)
	Euros = (50000,20000,10000,5000,2000,1000,500,200,100,50,20,10,5,2,1)
	Yen = (100000,50000,20000,10000,5000,1000,500,100,50,10)
	Pounds = (5000,2000,1000,500,200,100,50,20,10,5,1)

	question = input("Select your currency (type '?' for options), or type 'custom' to add one: ")
	if (question == "?"):
		currencies = ("-dollars", "-euros", "-yen", "-pounds", "-custom", "*all lowercase")

		for words in currencies:

		     print(words)
		count()
	elif (question == "dollars"):
		currency = Dollars
	elif (question == "euros"):
		currency = Euros
	elif (question == "yen"):
		currency = Yen
	elif (question == "pounds"):
		currency = Pounds
	elif (question == "custom"):
		num = input("Okay. Now, please provide coins/bills values separated by commas. e.g. 100,20,0.25: ")
		C_list = list(map(float,num.split(',')))
		CustomCurrency = tuple(sorted([i * 100 for i in C_list], reverse = True))
		currency = CustomCurrency
	else:
		print("Currency not recognized, try again.")
		count()


	total = 100*eval(input("What is the total ammount of money (in your currency)? "))
	coinsE = 0
	for i in currency:
		coins, remain = divmod(total,i)
		total = round(remain)
		coinsE += coins
	if (remain == 0):
		print("You need at least ", coinsE, " coins/bills to match that ammount.")
	else:
		print("Your currency or total is defective, you can't match that ammount.")
	returnC = input("Do you want to evaluate a different change? (yes/no) ")
	if (returnC == "yes"):
		count()
	else: 
		input("Press ENTER to return to the main screen")
		return

