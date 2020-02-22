# Hearthstone Card Pack Opening Simulator
# Create 5 card objects
# Assign each card a rarity based on official Blizzard Numbers
# 1 rare or better in every pack, epic is 1 in 5 packs, legendary is 1 in 20 packs
# For each of the cards, depending on rarity, randomly choose a card from that database
# If first 4 cards are common, run the rarity test on 5th card. If common, make it rare. Else leave it.
# Display information back to user
# Repeat if player clicks "draw again"

import random
commons=[]
rares=[]
epics=[]
legendaries=[]

class Card:
	def __init__(self, name, rarity, pos):
		self.name = name
		self.rarity = rarity
		self.pos = pos

	def setName(self, newName):
		self.name = newName

	def getName(self):
		return self.name

	def printName(self):
		return print(str(self.name))

	def setRarity(self):
		n = random.randint(1,100)
		if (n == 1):
			self.rarity = "legendary"
			return
		else:
			n = random.randint(1,25)
			if (n==1):
				self.rarity = "epic"
				return
			else:
				n = random.randint(1,5)
				if (n==1):
					self.rarity = "rare"
					return
				else:
					self.rarity = "common"
					return
	def getRarity(self):
		return self.rarity

	def forceRare(self):
		self.rarity = "rare"

	def printCard(self):
		print(self.name, self.rarity, sep=" - ")


def main():

	check = input("Enter 'a' to open a pack: ")
	print()
	while (check == 'a'):
		openPack()
		print()
		check = input("Enter 'a' to open another, 's' for statistics, any other key to exit...")
		print()
		if (check == 's'):
			displayStats()
			print()
			check = input("Enter 'a' to open another, any other key to exit...")
			if (check != 'a'):
				break
			else:
				continue



def openPack():
	fileCommon = open("common.txt", "r")
	common = fileCommon.readlines() 
	numCommon = len(common)

	fileRare = open("rare.txt", "r")
	rare = fileRare.readlines() 
	numRare = len(rare)

	fileEpic = open("epic.txt", "r")
	epic = fileEpic.readlines() 
	numEpic = len(epic)

	fileLegendary = open("legendary.txt", "r")
	legendary = fileLegendary.readlines() 
	numLegendary = len(legendary)
	

	newCards = []
	for x in range(0,5):
		x = Card("","","")
		Card.setRarity(x)
		newCards.append(x)

	if (Card.getRarity(newCards[0]) == "common"):
		if (Card.getRarity(newCards[1]) == "common"):
			if (Card.getRarity(newCards[2]) == "common"):
				if (Card.getRarity(newCards[3]) == "common"):
					Card.forceRare(newCards[4])


	for y in newCards:
		rarity = Card.getRarity(y)
		if (rarity == "common"):
			n = random.randint(0,numCommon-1)
			newName = common[n]
			Card.setName(y, newName)
			commons.append(y)

		if (rarity == "rare"):
			n = random.randint(0,numRare-1)
			newName = rare[n]
			Card.setName(y, newName)
			rares.append(y)

		if (rarity == "epic"):
			n = random.randint(0,numEpic-1)
			newName = epic[n]
			Card.setName(y, newName)
			epics.append(y)

		if (rarity == "legendary"):
			n = random.randint(0,numLegendary-1)
			newName = legendary[n]
			Card.setName(y, newName)
			legendaries.append(y)

		Card.printCard(y)

def displayStats():
	totalCards = len(commons) + len(rares) + len(epics) + len(legendaries)
	print('\nTotal Cards Opened: ', totalCards)
	print()
	print('Total Commons: ', len(commons))
	for x in commons:
		print(Card.getName(x))
	print()
	print('Total Rares: ', len(rares))
	for x in rares:
		print(Card.getName(x))
	print()
	print('Total Epics: ', len(epics))
	for x in epics:
		print(Card.getName(x))
	print()
	print('Total Legendaries: ', len(legendaries))
	for x in legendaries:
		print(Card.getName(x))
	print()



if __name__ == '__main__':
	main()


