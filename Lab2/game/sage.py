import path_objects as P
import action 

def get_input():
	command = input("> ").split()
	verb_word = command[0]

	if (verb_word in action.verb_dict):
		verb = action.verb_dict[verb_word]
	else:
		print("I don't know how to {}".format(verb_word))
		return

	if len(command) >= 2:
		noun_word = command[1]
		print(verb(noun_word))
	else:
		print(verb("nothing"))

print("welcum")
while True:
	get_input()
	action.time()

