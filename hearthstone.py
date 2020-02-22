# Hearthstone Card Pack Opening Simulator
# Created by Matthew Thibodeau - University of South Florida - 2/22/2020

# First Create 5 card objects
# Assign each card a rarity based on official Blizzard Numbers
# 1 rare or better in every pack, epic is 1 in 5 packs, legendary is 1 in 20 packs
# For each of the cards, depending on rarity, randomly choose a card from that database
# If first 4 cards are common, run the rarity test on 5th card. If common, make it rare. Else leave it.
# Display information back to user
# Repeat if player clicks "draw again"

#Random library will be needed for this project
import random

#Set up lists to contain all of the drawn cards
commons=[]
rares=[]
epics=[]
legendaries=[]

#The Card class defines each card based on its name and rarity
class Card:
	def __init__(self, name, rarity):
		self.name = name
		self.rarity = rarity

	def setName(self, newName):
		self.name = newName

	def getName(self):
		return self.name

	def printName(self):
		return print(str(self.name))

#The setRarity function uses an algorithm to decide each cards rarity
#Odds per card are 1% Legendary, 4% epic, and 20% rare
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

#The force rare function is used later on to guarantee one rare per pack
	def forceRare(self):
		self.rarity = "rare"

	def printCard(self):
		print(self.name, self.rarity, sep=" - ")


#We want to make sure the user has the option to check their statistics
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

#All of the card names are taken from .txt files
#We will also need the length of the text files for random num generation
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
	

#Create a list to store the new cards in and generate their rarity
	newCards = []
	for x in range(0,5):
		x = Card("","")
		Card.setRarity(x)
		newCards.append(x)

#This algorithm guarantees a rare in the event that 4 commons were drawn in a row
	if (Card.getRarity(newCards[0]) == "common"):
		if (Card.getRarity(newCards[1]) == "common"):
			if (Card.getRarity(newCards[2]) == "common"):
				if (Card.getRarity(newCards[3]) == "common"):
					Card.forceRare(newCards[4])


#Check the rarity of each card, assign it a random name from .txt file based on rarity
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

#Function to display all the statistics about your run so far
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


