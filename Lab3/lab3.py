# Juan P. Prieto
# Lab 3

from random import randint
from time import sleep

# global variable of chutes and ladders
# chutes and ladders playable up to a 16*16 board.
chutes_ladders = {4:7, 8:15, 12:2, 14:6, 21:42, 28:84, 36:44,
                  47:26, 49:11, 51:67, 56:53, 62:19, 64:60,
                  71:91, 80:100, 87:24, 93:73, 95:75, 98:78, 
                  109:117, 124:94, 136:142, 153:177, 170:115, 
                  180:164, 199:1, 212:230, 234:198, 247:233}

winner = ""

# Rolls a die of six sides and returns the result
def roll_die():
	return(randint(1,6))

# makes a game (just a list) of the given dimensions
def makeGame(w, l):
	return(list(range(w*l)))

# checks if given square is a chutes or ladders
def is_chutes_ladders(d):
	if chutes_ladders[d]>d:
		return("ladder")
	else:
		return("chute")


# function to make and play a game
def play_game(mode, l, w):
	global winner
	if mode == "simulation":
		state = {"state" : 1, "moves" : 0}
		while True:
			roll = roll_die()
			state["state"] += roll
			state["moves"] += 1
			if state["state"]>=len(makeGame(w,l)):
				break
		return(state["moves"])
	else:
		playernum = eval(input("How many players will be participating? "))
		state = []# This should be a list of dictionaries of each player's state
		for i in range(playernum):
			name = input("Player {} name: ".format(i + 1))
			state.append({"player" : name, "state" : 1, "moves" : 0})
		print()
		while winner == "":
			for i in range(playernum):
				input("Press ENTER to roll the dice, {}... ".format(state[i]["player"]))
				roll = roll_die()
				state[i]["state"] += roll 
				print("You rolled a {}.".format(roll))
				if state[i]["state"] >= len(makeGame(w,l)):
					winner = state[i]["player"]
					break
				if state[i]["state"] in chutes_ladders:
					static = state[i]["state"]
					state[i]["state"] = chutes_ladders[static]
					proper = is_chutes_ladders(static)
					if proper == "chute":
						print("Oh no, a chute in {}. You went down to {}".format(static, state[i]["state"]))
					else:
						print("Up we go! You climbed the ladder in {} up to {}.".format(static, state[i]["state"]))
				else:
					print("You are now in square {}".format(state[i]["state"]))
				sleep(2)
				print("-------------------------------------")
		print("Congratulations {}, you won!".format(winner))

# Runs the game as a simulation and keeps track of the number of moves it takes to win and returns average
def simulate_game(l, w):
	runnum = int(input("How many runs would you want to simulate? "))
	runs = []
	for i in range(runnum):
		mode = "simulation"
		runs.append(play_game(mode, l, w))
	print("The average number of moves to win was:", sum(runs) / len(runs))

def main():
	global chutes_ladders
	mode = input("Please indicate mode ('play' or 'simulation'): ")
	if mode == "simulation":
		l, w = eval(input("indicate lenght and width of game (respectivelly), separated by commas: "))
		simulate_game(l, w)
	else:
		l, w = eval(input("indicate lenght and width of game (respectivelly), separated by commas: "))
		play_game("play", l, w)

if __name__ == "__main__":
	main()
