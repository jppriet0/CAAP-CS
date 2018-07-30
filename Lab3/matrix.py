# takes the number of rows and columns and makes a matrix of those dimensions
from lab3 import chutes_ladders
from decimal import *

def make_matrix(r, c):
	matrix = [[0 for x in range(r)] for y in range(c)]
	for row in range(r):	#This will create the probabilities with a 6 side fair die, for a game of any dimension
		try:
			for col in range(row+1, row+7):
				if col+1 in chutes_ladders:
					matrix[row][chutes_ladders[col+1]-1] += 0.2 
				else:
					matrix[row][col] += 0.2
		except IndexError:
			matrix[row][c-1] += round(1-sum(matrix[row]),1)
	return(matrix)

def makeidentity(c):
	identitym = [1]
	for i in range(c-1):
		identitym.append(0)
	return(identitym)

# takes two matrices and multiplies them returnin the resulting matrix
def matrixmult(a,b):
	try:	
		a[0][0]
		#Got this matrix multiplier function idea online, I adapted it. The zip and * unpacking are useful for other programs. This does not work for a 1*x times x*x matrix, though.
		multimatrix = [[sum(x*y for x,y in zip(a_row,b_col)) for b_col in zip(*b)] for a_row in a]
		return(multimatrix)
	except TypeError:
		multimatrix = []
		#This function I made myself from what I learned from the other, it didn't need zip or *, though.
		for i in range(len(a)):
			res = [a[x]*b[x][i] for x in range(len(a))]
			multimatrix.append(sum(res))
		return(multimatrix)

# prints the given matrix, mostly for testing purposes
def print_matrix(m):
		for ra in range(len(m[0])):
			matrixmap = []
			for ce in range(len(m)):
				matrixmap.append(m[ra][ce])
			print(matrixmap)

# given a state matrix, and a transition matrix, runs a markov simulation of the game and returns average number of moves.  
def markov_simulation():
	r, c = eval(input("What are the dimensions of the game? (rows and columns separated by commas) "))
	print("game size:", r*c)
	markov = makeidentity(r*c)
	probmat = make_matrix(r*c,r*c)
	m_turns = 0
	while markov[(r*c)-1]<0.99:
		m_turns += 1
		markov = matrixmult(markov,probmat)
		print("probability of win after {} round:".format(m_turns), markov[r*c-1])
	return("it took {} turns to win with 99 percent confidence. ".format(m_turns))

def printb(m):
	lis = []
	for i in range(len(m)):
		lis.append(i)
	print(lis)


print(markov_simulation())