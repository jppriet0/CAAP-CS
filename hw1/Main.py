def welcome():
	program = input("What program do you want to use? (type '?' for a list of programs)... ")

	if (program == "?"):
		list = ("- Hello: Type 'hello'", "- Celsius/farenheit converter: Type: 'temp'", "- Parsec/light year converter: Type 'astro'", "- Sigma (sum calculator): Type: 'sigma'", "- Fibonnaci term finder: Type 'fibo'", "- Coin change # calculator: Type: 'coins'", "To exit, write 'exit'" )

		for words in list:

		     print(words)

		welcome()
	elif (program == "hello"):
		print("")
		print("-----------------------------------------------------------")
		print("")
		try:
			import Hello
			Hello.Hello()
		except:
			input("Sorry, an error has been found. Press ENTER to return to the main screen")
		print("")
		print("-----------------------------------------------------------")
		print("")
		welcome()
	elif (program == "temp"):
		print("")
		print("-----------------------------------------------------------")
		print("")
		try:
			import tempcon
			tempcon.convertT()
		except:
			input("Sorry, an error has been found. Press ENTER to return to the main screen")
		print("")
		print("-----------------------------------------------------------")
		print("")
		welcome()
	elif (program == "astro"):
		print("")
		print("-----------------------------------------------------------")
		print("")
		try:
			import astrocon
			astrocon.convertA()
		except:
			input("Sorry, an error has been found. Press ENTER to return to the main screen")
		print("")
		print("-----------------------------------------------------------")
		print("")
		welcome()
	elif (program == "sigma"):
		print("")
		print("-----------------------------------------------------------")
		print("")
		try:
			import Sigma
			Sigma.sigma()
		except:
			input("Sorry, an error has been found. Press ENTER to return to the main screen")
		print("")
		print("-----------------------------------------------------------")
		print("")
		welcome()
	elif (program == "fibo"):
		print("")
		print("-----------------------------------------------------------")
		print("")
		try:
			import Fibonnaci
			Fibonnaci.main()
		except:
			input("Sorry, an error has been found. Press ENTER to return to the main screen")
		print("")
		print("-----------------------------------------------------------")
		print("")
		welcome()
	elif (program == "coins"):
		print("")
		print("-----------------------------------------------------------")
		print("")
		try:
			import coins
			coins.count()
		except:
			input("Sorry, an error has been found. Press ENTER to return to the main screen")
		print("")
		print("-----------------------------------------------------------")
		print("")
		welcome()
	elif (program == "exit"):
		exit()
	else: 
		print("Program not available, verify name")	
		welcome()    

welcome()