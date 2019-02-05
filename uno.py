from pprint import pprint

class Card:

	def __init__(self, color, attr):
		self.attr = attr
		self.color = color
		self.description = "This is a {0} colored {1}".format(self.color, self.attr,)

deck = []

player_hand = []

def create_deck():
	color_list = ["Blue", "Yellow", "Red", "Green"]
	effects = ["Skip", "Reverse", "Draw +2"]

	for color in color_list:
		card_color = color

		# Makes 0 card
		card_number = 0
		deck.append(Card(card_color, card_number))

		# Makes 1-9 * 2
		for i in range(1, 10):
			card_number = i
			deck.append(Card(card_color, card_number))
			deck.append(Card(card_color, card_number))

		# Makes skips, reverses, draw cards 
		for effect in effects:
			card_effect = effect
			deck.append(Card(card_color, card_effect))
			deck.append(Card(card_color, card_effect))

	# Makes wild cards
	for i in range(0, 4):
		deck.append(Card("Wild", "Wild"))
		deck.append(Card("Wild", "Wild +4"))

def draw_card():
	pass

def shuffle_deck():
	pass

if __name__ == '__main__':
	create_deck()
	for card in deck:
		pprint(card.description)
		
	pprint(len(deck))
