import random


#Starting Point for Game Program.
#card values
numbers=["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
suits=["Heart", "Diamond", "Club", "Spade"]
#This is deck of cards
card_deck =[]
#This is cards to player from deck.
delt_cards=[]
#This is cards to dealer from deck.
dealer_cards = []
#Player sum of cards
player_sum=0
#dealer sum of cards
daler_sum = 0

#get deck of cards.
def get_card_deck():
	for number in numbers:
		for suit in suits:
			card_deck.append([number,suit])
			
#Shuffle deck of cards.
def Shuffle_deck():
	random.shuffle(card_deck)
	
#Deal two cards to player from deck
def deal_player_cards():
	a1 = card_deck.pop(0)
	a2 = card_deck.pop(0)
	delt_cards =[a1,a2]
	
	return delt_cards

		
#Deal two cards to Dealer from deck
def  deal_dealer_cards():
	a1 = card_deck.pop(0)
	a2 = card_deck.pop(0)
	dealer_cards =[a1,a2]
	
	return dealer_cards
	
#get sum of first player cards delt
def get_player_sum():
	sum = 0
	for number, suit in delt_cards:
		if number == "J":
			number = 10
		elif number == "Q":
			number = 10
		elif number == "K":
			number = 10
		elif number == "A":
			choice= int(input("What amount do yo want A to be? 1 or 11?\n"))
			number = choice	
		sum = sum + number
		player_sum=sum
		
	return player_sum


#get sum of player cards after hit
def get_new_player_sum(player_sum, delt_cards):
	a=delt_cards[-1]

	if a[0]== "J":
		a[0] = 10
	elif a[0] == "Q":
		a[0] = 10
	elif a[0] == "K":
		a[0] = 10
	elif a[0] == "A":
		a[0]= int(input("What amount do yo want A to be? 1 or 11?\n"))
		
	player_sum = player_sum + a[0]

	return player_sum
		
	
#get dealer summ of first cards
def get_dealer_sum():
	sum = 0
	for number, suit in dealer_cards:
		if number == "J":
			number = 10
		elif number == "Q":
			number = 10
		elif number == "K":
			number = 10
		elif number == "A":
			if sum + 11 < 21:
				number = 11
			elif sum + 1 < 21:
				number = 1		
		sum = sum + number
		dealer_sum=sum
		
	return dealer_sum


#hit player cards
def hit_me():
	while True:	
		hit=(input('If you want to hit press "y", if you want to stay press "n".'))
		if hit =="y":
			delt_cards.append(card_deck.pop(0))
			break
		elif hit == "n":
			print ("I will stay.")
			break
		else:
			print ("Please select a y for hit or n for stay")
		
		print()
	return delt_cards	


#Actual Game :

#get Deck
get_card_deck()
#Shuffle deck
Shuffle_deck()
#get first two dealt player and dealer cards
delt_cards=deal_player_cards()
dealer_cards=deal_dealer_cards()
#display dealers cards
print("Dealer cards are:")
print(dealer_cards)
#get dealer sum from first cards delt to dealer
dealer_sum = get_dealer_sum()
print("\n")
#display player cards
print("Your cards are:")
print (delt_cards)
#get player sum from first cards delt to player
player_sum = get_player_sum()
print (f"Your card total is {player_sum}.")
print()

while player_sum <= 21:
#hit player
	hit_me()
	print()
#display new set of cards of player
	print(delt_cards)
#get new sum of player cards with hit
	player_sum = get_new_player_sum(player_sum, delt_cards)
	print (f"Your card total is {player_sum}.")
	





