import path_objects as P
darkness = 0
turn = 0
sanity = 7

def say(noun):
	global turn
	turn += 1
	if turn == 1:
		print('turned')
	return('You said "{}"'.format(noun))

def examine(noun):
	global turn
	turn += 1
	if (darkness >= 2):
		return("It is too dark to see anything")
	else:
		if noun in P.GameObject.objects:
			return P.GameObject.objects[noun].get_desc()
		else:
			return('There is no "{}" here'.format(noun))

def kill(noun):
	global turn
	turn += 1
	#del P.GameObject.objects[noun]
	#P.GameObject.objects[noun].desc = "I hoep"
	return("fucking tes")

def hint(noun):
	global turn
	turn += 1
	#del P.GameObject.objects[noun]
	#P.GameObject.objects[noun].desc = "I hoep"
	return("fucking tes")

def look(noun):
	global turn
	turn += 1
	return("You cannot see anything...")

def search(noun):
	global turn
	turn += 1
	if noun in P.GameObject.objects:
		return ("P.GameObject.objects[noun].get_desc()")
	else:
		return('There is no "{}" here'.format(noun))

def inventory(noun):
	global turn
	turn += 1
	#del P.GameObject.objects[noun]
	#P.GameObject.objects[noun].desc = "I hoep"
	return("fucking tes")

def take(noun):
	global turn
	turn += 1
	#del P.GameObject.objects[noun]
	#P.GameObject.objects[noun].desc = "I hoep"
	return("fucking tes")

def drop(noun):
	global turn
	turn += 1
	#del P.GameObject.objects[noun]
	#P.GameObject.objects[noun].desc = "I hoep"
	return("fucking tes")

def listen(noun):
	global turn
	turn += 1
	#del P.GameObject.objects[noun]
	#P.GameObject.objects[noun].desc = "I hoep"
	return("fucking tes")

def touch(noun):
	global turn
	turn += 1
	#del P.GameObject.objects[noun]
	#P.GameObject.objects[noun].desc = "I hoep"
	return("fucking tes")

def smell(noun):
	global turn
	turn += 1
	#del P.GameObject.objects[noun]
	#P.GameObject.objects[noun].desc = "I hoep"
	return("fucking tes")

def taste(noun):
	global turn
	turn += 1
	#del P.GameObject.objects[noun]
	#P.GameObject.objects[noun].desc = "I hoep"
	return("fucking tes")

def openx(noun):
	global turn
	turn += 1
	#del P.GameObject.objects[noun]
	#P.GameObject.objects[noun].desc = "I hoep"
	return("fucking tes")

def close(noun):
	global turn
	turn += 1
	#del P.GameObject.objects[noun]
	#P.GameObject.objects[noun].desc = "I hoep"
	return("fucking tes")

def zzz(noun):
	global turn
	turn += 1
	#del P.GameObject.objects[noun]
	#P.GameObject.objects[noun].desc = "I hoep"
	return("fucking tes")

def think(noun):
	global turn
	turn += 1
	#del P.GameObject.objects[noun]
	#P.GameObject.objects[noun].desc = "I hoep"
	return("fucking tes")

def save(noun):
	global turn
	turn += 1
	#del P.GameObject.objects[noun]
	#P.GameObject.objects[noun].desc = "I hoep"
	return("fucking tes")

def restore(noun):
	global turn
	turn += 1
	#del P.GameObject.objects[noun]
	#P.GameObject.objects[noun].desc = "I hoep"
	return("fucking tes")

def quit(noun):
	global turn
	turn += 1
	#del P.GameObject.objects[noun]
	#P.GameObject.objects[noun].desc = "I hoep"
	return("fucking tes")

def read(noun):
	global turn
	turn += 1
	#del P.GameObject.objects[noun]
	#P.GameObject.objects[noun].desc = "I hoep"
	return("fucking tes")

def score(noun):
	global turn
	turn += 1
	#del P.GameObject.objects[noun]
	#P.GameObject.objects[noun].desc = "I hoep"
	return("fucking tes")

def positive(noun):
	global turn
	turn += 1
	#del P.GameObject.objects[noun]
	#P.GameObject.objects[noun].desc = "I hoep"
	return("fucking tes")

def negative(noun):
	global turn
	turn += 1
	#del P.GameObject.objects[noun]
	#P.GameObject.objects[noun].desc = "I hoep"
	return("fucking tes")

def shake(noun):
	global turn
	turn += 1
	if noun in P.GameObject.objects:
		return (P.GameObject.objects[noun].shook())
	else:
		return('There is no "{}" here'.format(noun))
	#del P.GameObject.objects[noun]
	#P.GameObject.objects[noun].desc = "I hoep"

#def negative(noun):
	#del P.GameObject.objects[noun]
	#P.GameObject.objects[noun].desc = "I hoep"
	#return("fucking tes")


verb_dict = {
	"say": say,
	"examine": examine,
	"kill": kill,
	"hint": hint,
	"look": look,
	"search": search,
	"find": search,
	"inventory": inventory,
	"take": take,
	"drop": drop,
	"listen": listen,
	"touch": touch,
	"smell": smell,
	"taste": taste,
	"open": openx,
	"close": close,
	"wait": zzz,
	"think": think,
	"save": save,
	"restore": restore,
	"quit": quit,
	"q": quit,
	"read": read,
	"score": score,
	"cert": positive,
	"nert": negative,
	"shake": shake,
}

def time():
	global turn
	global darkness
	global sanity
	if darkness<3:
		turn += 1
		darkness += 1
	elif darkness>=4:
		sanity -= 1

	if sanity == 0:
		print("ok")



