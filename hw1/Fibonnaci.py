def Fib(n):
	if (n == 0):
		return 0
	elif (n == 1):
		return 1
	else:
		return Fib(n-1) + Fib(n-2)

def main():
	n = eval(input("Input your number of Fibonacci term: "))
	print("That Fibbonaci term corresponds to the number: ", Fib(n))
	returnF = input("Do you want to find another term? (yes/no) ")
	if (returnF == "yes"):
		main()
	else: input("Press ENTER to return to the main screen")
	