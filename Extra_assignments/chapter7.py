#chapter 7 exercises

#2.
def grade():
	quiz = int(eval(input("What was your score? "))/20)
	letters = {0:"F",1:"F",2:"D",3:"C",2:"B",1:"A"}
	return(letters[quiz])
#4.
def standing():
	cred = eval(input("How many credits do you have? "))
	if cred < 7:
		return("Freshman")
	elif cred < 16:
		return("Sophomore")
	elif cred < 26:
		return("Junior")
	else:
		return("Senior")
#6. 
def fine():
	speed = eval(input("What was the speed? "))
	lim = evalI(input("What is the speed limit? "))
	if speed > lim:	
		if speed < 90:
			return(50+5*(lim-speed))
		else:
			return(250+5*(lim-speed))
#8.
def eligible():
	age = eval(input("What is your age? "))
	citi = eval(input("For how long have you been an U.S citizen? "))
	if age > 30 and citi > 9:
		return("You are eligible for Senate and House")
	elif age > 25 and citi > 7:
		return("You are eleigible for the House, only")
	else:
		return("You are not eligible for anything")

#10.
def easter():
	year = eval(input("What is the year to calculate easter? "))
	a = year%19
	b = year%4
	c = year%7
	d = (19*a+24)%30
	e = (2*b + 4*c + 6*d + 5)%7
	day = 22 + d + e
	badyears = [1954,1981,2049,2076]
	if year in badyears:
		day -= 7
		if 0<day<31:
			return("Easter will be on March {}".format(day))
		else:
			return("Easter will be on April {}".format(day-31))
	else:
		if 0<day<31:
			return("Easter will be on March {}".format(day))
		else:
			return("Easter will be on April {}".format(day-31))

#print(easter())

#12.
def dateev():
	date = input("input date MM/DD/YYYY: ").split("/")
	if int(date[0]) == 1 or int(date[0]) == 3 or int(date[0]) == 5 or int(date[0]) == 7 or int(date[0]) == 8 or int(date[0]) == 10 or int(date[0]) == 12:
		if int(date[1])>31:
			return("invalid")
		else:
			return("valid")
	elif int(date[0]) == 2:
		if int(date[1])<28:
			return("valid")
		elif int(date[1])<29:
			return("valid, but only in leap years")
		else:
			return("invalid")
	elif int(date[0]) > 12:
		return("invalid")
	else:
		if int(date[1])>30:
			return("invalid")
		else:
			return("valid")
