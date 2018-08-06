# YOUR NAME
# Assignemnt X
# Date Due

# Imports the turtle graphics module
import turtle
 
# creates a turtle (pen) an sets the speed (where 0 is fastest and 10 is slowest)
# The colors can be set through their names or through hexadecimal codes, use hex for accuracy
myPen = turtle.Turtle()
myPen.speed(0)
myPen.color("#000000")
turtle.tracer(5)

# setting out box sizes to the n sq pixels per box
Size1 = 10
Size3 = 30 #for Pacman ghost painting
 

# myPen.setheading(n) points pen to given angle direction.
# where n queals the angle.
# 0 points to the right, 90 to go up, 180 to go to the left 270 to go down

# Positions myPen in top left area of the screen
# This should change according to the image size you want to make and the size of your boxes ("pixels")
# This canvas is currently set to 200*200 pixels or a 20x20 box of 10 sq pixels each
myPen.penup()
myPen.forward(-100)
myPen.setheading(90)
myPen.forward(100)
myPen.setheading(0) 

# This function draws a box by drawing each side of the square and using the fill function
def box(intDim):
	dire = myPen.heading()
	myPen.begin_fill()
	# 0 deg.
	myPen.forward(intDim)
	myPen.left(90)
	# 90 deg.
	myPen.forward(intDim)
	myPen.left(90)
	# 180 deg.
	myPen.forward(intDim)
	myPen.left(90)
	# 270 deg.
	myPen.forward(intDim)
	myPen.end_fill()
	myPen.setheading(dire)	   

# Here is an example of how to draw a box using the box function	  
# Comment this out when you draw your own images
#box(boxSize)
 

# Challenge functions (2 bonus pts each) 
# You need to make shapes with each
#def circle(intRadius):
#def triangle(intLength): #This can be an equilateral triangle
#def save_image(): # saves the screen to an image/vector file

# These are the instructions on how to move "myPen" around after drawing a box.
# penup() lifts the pen so it doesn't draw anything and can be moved freely
# pendown() puts the oen down and it draws as it moves
# myPen.penup()
# myPen.forward(boxSize)
# myPen.pendown()
 
# You will save your drawings as lists.
# This first list stores the color values
pallet_1 = ["#FFFFFF" , "#FFFF00" , "#000000" , "#61380B" , "#F4FA58"]
# Your drawings are stored using a "list of lists" where each value within every list
# element is the index of the color in the pallet list
# Banana
pixels_1 = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
pixels_1.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,0,0,0,0,2,2,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,0,0,2,2,3,3,2,0,0,0,0,0])
pixels_1.append([0,0,0,0,0,2,4,1,2,2,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,2,4,4,1,2,0,0,0,0,0,0,0])
pixels_1.append([0,0,0,2,4,4,1,2,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,2,4,4,4,1,2,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,2,4,1,1,2,0,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,2,4,4,1,2,0,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,0,2,4,1,1,2,2,2,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,2,4,1,3,2,0,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,0,2,2,2,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

# Mario
pallet_2 = ["#4B610B" , "#FAFAFA" , "#DF0101" , "#FE9A2E"]
pixels_2 = [[1,1,1,1,2,2,2,2,2,2,2,2,1,1,1,1]]
pixels_2.append([1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,1])
pixels_2.append([1,1,1,0,0,0,3,3,3,3,3,0,3,1,1,1])
pixels_2.append([1,1,0,3,0,3,3,3,3,3,3,0,3,3,3,1])
pixels_2.append([1,1,0,3,0,0,3,3,3,3,3,3,0,3,3,3])
pixels_2.append([1,1,0,0,3,3,3,3,3,3,3,0,0,0,0,1])
pixels_2.append([1,1,1,1,3,3,3,3,3,3,3,3,3,3,1,1])
pixels_2.append([1,1,1,0,0,2,0,0,0,0,2,0,1,1,1,1])
pixels_2.append([1,1,0,0,0,2,0,0,0,0,2,0,0,0,1,1])
pixels_2.append([0,0,0,0,0,2,2,2,2,2,2,0,0,0,0,0])
pixels_2.append([3,3,3,0,2,3,2,2,2,2,3,2,0,3,3,3])
pixels_2.append([3,3,3,3,2,2,2,2,2,2,2,2,3,3,3,3])
pixels_2.append([3,3,3,2,2,2,2,1,1,2,2,2,2,3,3,3])
pixels_2.append([1,1,1,2,2,2,1,1,1,1,2,2,2,1,1,1])
pixels_2.append([1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1])
pixels_2.append([0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0])

# Space
pallet_blank = ["#FFFFFF"]
pixels_blank = [[0],[0],[0]]

# Pacman Ghost
pallet_red = ["#FFFFFF", "#FF0800", "#0000FF"]
pixels_ghost = [[0,0,0,0,0,1,1,1,1,1,1,0,0,0]]
pixels_ghost.append([0,0,0,1,1,1,1,1,1,1,1,1,0,0])
pixels_ghost.append([0,0,1,1,0,0,1,1,1,1,0,0,1,0])
pixels_ghost.append([0,1,1,0,0,0,0,1,1,0,0,0,0,0])
pixels_ghost.append([0,1,1,0,0,2,2,1,1,0,0,2,2,0])
pixels_ghost.append([1,1,1,0,0,2,2,1,1,0,0,2,2,1])
pixels_ghost.append([1,1,1,1,0,0,1,1,1,1,0,0,1,1])
pixels_ghost.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1])
pixels_ghost.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1])
pixels_ghost.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1])
pixels_ghost.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1])
pixels_ghost.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1])
pixels_ghost.append([1,1,0,1,1,1,0,0,1,1,1,0,1,1])
pixels_ghost.append([1,0,0,0,1,1,0,0,1,1,0,0,0,1])

# Invader
pallet_black = ["#FFFFFF", "#000000"]
pixels_invader = [[0,0,1,0,0,0,0,0,1,0,0]]
pixels_invader.append([0,0,0,1,0,0,0,1,0,0,0])
pixels_invader.append([0,0,1,1,1,1,1,1,1,0,0])
pixels_invader.append([0,1,1,0,1,1,1,0,1,1,0])
pixels_invader.append([1,1,1,1,1,1,1,1,1,1,1])
pixels_invader.append([1,0,1,1,1,1,1,1,1,0,1])
pixels_invader.append([1,0,1,0,0,0,0,0,1,0,1])
pixels_invader.append([0,0,0,1,1,0,1,1,0,0,0])

# Shroom
pallet_shroom = ["#FFFFFF", "#000000", "#FF0800"]
pixels_shroom = [[0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0]]
pixels_shroom.append([0,0,0,1,1,2,2,2,2,0,0,1,1,0,0,0])
pixels_shroom.append([0,0,1,0,0,2,2,2,2,0,0,0,0,1,0,0])
pixels_shroom.append([0,1,0,0,2,2,2,2,2,2,0,0,0,0,1,0])
pixels_shroom.append([0,1,0,2,2,0,0,0,0,2,2,0,0,0,1,0])
pixels_shroom.append([1,2,2,2,0,0,0,0,0,0,2,2,2,2,2,1])
pixels_shroom.append([1,2,2,2,0,0,0,0,0,0,2,2,0,0,2,1])
pixels_shroom.append([1,0,2,2,0,0,0,0,0,0,2,0,0,0,0,1])
pixels_shroom.append([1,0,0,2,2,0,0,0,0,2,2,0,0,0,0,1])
pixels_shroom.append([1,0,0,2,2,2,2,2,2,2,2,2,0,0,2,1])
pixels_shroom.append([1,0,2,2,1,1,1,1,1,1,1,1,2,2,2,1])
pixels_shroom.append([0,1,1,1,0,0,1,0,0,1,0,0,1,1,1,0])
pixels_shroom.append([0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0])
pixels_shroom.append([0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0])
pixels_shroom.append([0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0])
pixels_shroom.append([0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0])

# Happy face

pallet_sm = ["#FFFFFF", "#000000", "#FFE938", "#C2931F", "#F8B3DE"]
pixels_sm =     [[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0]]
pixels_sm.append([0,0,0,0,0,0,0,0,0,0,1,1,1,2,2,2,2,2,1,1,1,0,0,0,0,0,0,0,0,0,0])
pixels_sm.append([0,0,0,0,0,0,0,0,1,1,2,2,2,2,2,2,2,2,2,2,2,1,1,0,0,0,0,0,0,0,0])
pixels_sm.append([0,0,0,0,0,0,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,0,0,0,0,0,0])
pixels_sm.append([0,0,0,0,0,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,0,0,0,0,0])
pixels_sm.append([0,0,0,0,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,0,0,0,0])
pixels_sm.append([0,0,0,1,2,2,2,1,1,1,1,2,2,2,2,2,2,2,2,1,1,1,1,1,2,2,2,1,0,0,0])
pixels_sm.append([0,0,0,1,2,2,1,1,1,1,0,1,2,2,2,2,2,2,1,1,1,1,0,0,1,2,2,1,0,0,0])
pixels_sm.append([0,0,1,2,2,1,1,1,1,1,0,0,1,2,2,2,2,1,1,1,1,1,0,0,0,1,2,2,1,0,0])
pixels_sm.append([0,0,1,2,2,1,1,1,1,1,0,0,1,2,2,2,2,1,1,1,1,1,0,0,0,1,2,2,1,0,0])
pixels_sm.append([0,1,2,2,2,1,1,1,1,0,0,0,1,2,2,2,2,1,1,1,1,0,0,0,0,1,2,2,2,1,0])
pixels_sm.append([0,1,2,2,1,0,0,0,0,0,0,0,0,1,2,2,1,0,0,0,0,0,0,0,0,0,1,2,2,1,0])
pixels_sm.append([0,1,2,2,1,0,0,0,0,0,0,0,0,1,2,2,1,0,0,0,0,0,0,0,0,0,1,2,2,1,0])
pixels_sm.append([1,2,2,2,1,0,0,0,0,0,0,0,0,1,2,2,1,0,0,0,0,0,0,0,0,0,1,2,2,2,1])
pixels_sm.append([1,2,2,2,1,1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,2,2,2,1])
pixels_sm.append([1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1])
pixels_sm.append([1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1])
pixels_sm.append([1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1])
pixels_sm.append([0,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,0])
pixels_sm.append([0,1,2,2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,2,2,1,0])
pixels_sm.append([0,1,2,2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,2,2,1,0])
pixels_sm.append([0,0,1,2,2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,2,2,1,0,0])
pixels_sm.append([0,0,1,2,2,1,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,3,3,3,3,1,2,2,1,0,0])
pixels_sm.append([0,0,0,1,2,2,1,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,3,3,1,2,2,1,0,0,0])
pixels_sm.append([0,0,0,1,2,2,2,1,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,1,2,2,2,1,0,0,0])
pixels_sm.append([0,0,0,0,1,2,2,2,1,1,3,3,3,3,4,4,4,4,4,4,4,1,1,2,2,2,1,0,0,0,0])
pixels_sm.append([0,0,0,0,0,1,2,2,2,2,1,1,1,3,4,4,4,4,1,1,1,2,2,2,2,1,0,0,0,0,0])
pixels_sm.append([0,0,0,0,0,0,1,1,2,2,2,2,2,1,1,1,1,1,2,2,2,2,2,1,1,0,0,0,0,0,0])
pixels_sm.append([0,0,0,0,0,0,0,0,1,1,2,2,2,2,2,2,2,2,2,2,2,1,1,0,0,0,0,0,0,0,0])
pixels_sm.append([0,0,0,0,0,0,0,0,0,0,1,1,1,2,2,2,2,2,1,1,1,0,0,0,0,0,0,0,0,0,0])
pixels_sm.append([0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0])

#Ying Yang
#Use Pallete_black
pixels_yy = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
pixels_yy.append([0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0])
pixels_yy.append([0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0])
pixels_yy.append([0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0])
pixels_yy.append([0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,0,0])
pixels_yy.append([0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,0,0])
pixels_yy.append([0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,0])
pixels_yy.append([0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,0])
pixels_yy.append([0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,0])
pixels_yy.append([0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,0])
pixels_yy.append([0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,0])
pixels_yy.append([0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0])
pixels_yy.append([0,0,1,1,1,0,0,0,0,1,1,0,0,0,0,1,0,0])
pixels_yy.append([0,0,1,1,1,0,0,0,0,1,1,0,0,0,1,1,0,0])
pixels_yy.append([0,0,0,1,1,1,0,0,0,0,0,0,0,1,1,0,0,0])
pixels_yy.append([0,0,0,0,1,1,1,1,0,0,0,0,1,1,0,0,0,0])
pixels_yy.append([0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0])

#Megaman
pallet_mega = {}
pixels_mega = [[]]
pixels_mega.append([0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0])
pixels_mega.append([0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0])
pixels_mega.append([0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0])
pixels_mega.append([0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0])
pixels_mega.append([0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0])
pixels_mega.append([0,0,0,0,1,1,1,1,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,1,1,0,0,0,0])
pixels_mega.append([0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0])
pixels_mega.append([0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,1,1,1,0,0,0,0,0,1,0,0])
pixels_mega.append([0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0])
pixels_mega.append([0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0])

# This function takes a pallet and pixel list (matrix) to draw the picture
# You are to write this function
def draw(pallet, pixels, size):
	posit_x, posit_y = myPen.position()
	for x_section in pixels:
		for pix in x_section:
			if pallet[pix] == "#FFFFFF":
				myPen.forward(size)
			else:
				myPen.color(pallet[pix])
				box(size)
				myPen.forward(size)
		myPen.goto(posit_x,posit_y-size)
		posit_x, posit_y = myPen.position()

def draw_shadow(pallet, pixels, size):
	posit_x, posit_y = myPen.position()
	init_x, init_y = posit_x, posit_y
	for x_section in pixels:
		for pix in x_section:
			if pallet[pix] == "#FFFFFF":
				myPen.forward(size)
			else:
				myPen.color("#CCCCCC")
				box(size)
				myPen.forward(size)
		myPen.goto(posit_x,posit_y-size)
		posit_x, posit_y = myPen.position()

	myPen.goto(init_x+(size/2),init_y-(size/2))
	posit_x, posit_y = myPen.position()
	for x_section in pixels:
		for pix in x_section:
			if pallet[pix] == "#FFFFFF":
				myPen.forward(size)
			else:
				myPen.color(pallet[pix])
				box(size)
				myPen.forward(size)
		myPen.goto(posit_x,posit_y-size)
		posit_x, posit_y = myPen.position()
# Should give the user a list of the possible drawing pieces you have and ask which one to draw
def main():
	#draw(pallet_1, pixels_1, Size1)
	#draw(pallet_2, pixels_2, Size1)
	#draw(pallet_red, pixels_ghost, Size1)
	#draw(pallet_blank, pixels_blank, Size1)
	#draw_shadow(pallet_green, pixels_invader, Size1)
	#draw(pallet_shroom,pixels_shroom, Size1)
	draw(pallet_black,pixels_mega,Size1)
	# You need this to prevent the window from closing after drawing
	turtle.done()

main()
