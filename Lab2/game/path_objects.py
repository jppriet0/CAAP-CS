class GameObject:
	class_name = ""
	desc = ""
	objects = {}

	def __init__(self, name):
		self.name = name
		GameObject.objects[self.class_name] = self

	def get_desc(self):
		return self.class_name + "\n\n" + self.desc

	def shook(self):
		if self.class_name == "fruit" && counter = 0:
			print("")
		else:
			print(self)

class Backpack(GameObject):
	class_name = "backpack"
	desc = "Your backpack, it contains a book, a magic crystal, and a scroll"
	state = "It is lying near you. You grab your backpack"

class SpellBook(GameObject):
	class_name = "book"
	desc = "The front cover of the book has the word 'SPELLS' written vertically down the left side in silver letters. There is some other writing as well, but it's too dark to make out. \n[To read the book, say 'next/prev', 'page <number>', or 'open/close book'.]"
	state = "It is inside your backpack"

class Crystal(GameObject):
	class_name = "crystal"
	desc = "A teardrop shaped crystal, lapizulli-colored, very beautiful"
	state = "It is inside your backpack"

class Scroll(GameObject):
	class_name = "scroll"
	desc = "A magic scroll with words you don't understant \n it shows someone pointing at a table while holding \n a teardrop shaped crystal"
	state = "It is inside your backpack"

class Fruit(GameObject):
	class_name = "fruit"
	desc = "It is hard and smooth, like ceramic."
	state = "You feel around and sense around looking for what fell, \n it is a fruit smaller than your fist. \n You grab it, it is hard and smooth, like ceramic."

u8ohas =  SpellBook("begginer's guide")
eigi = Fruit("your momma")

		