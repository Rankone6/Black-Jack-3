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
dealer_sum = 0
sum=0
play = "y"
cash = 0

def cash():
	cash= int(input("How much cash do yoy wanr to play with? $"))
	return cash


def get_shuffle_cards():
	#get deck of cards.
	for number in numbers:
		for suit in suits:
			card_deck.append([number,suit])
	
	#Shuffle deck of cards.
	random.shuffle(card_deck)
	
#get dealer cards
def get_dealer_cards():
	for i in range(2):
		dealer_cards.append(card_deck.pop(0))
		i=i+ 1
		
	return dealer_cards


#get player cards
def get_player_cards():
	for i in range(2):
		delt_cards.append(card_deck.pop(0))
		i=i+ 1
		
	return delt_cards

def get_player_number(sum):
	for number, suit in delt_cards:
		if number == "J":
			number = 10
		elif number == "Q":
			number = 10
		elif number == "K":
			number = 10
		elif number == "A":
			while True:	
				a = input("What amount do yo want A to be? 1 or 11?\n")
				if a == "1":
					number = 1
					break
				elif a == "11":
					number = 11
					break
				else:
					print('Please enter a "1" or or a "11".')
		sum = sum + number
		player_sum=sum
		
	return player_sum
	

def get_dealer_number(sum):
	for number, suit in dealer_cards:
		if number == "J":
			number = 10
		elif number == "Q":
			number = 10
		elif number == "K":
			number = 10
		elif number == "A":
			if sum + 11 <= 21:
				number = 11
			else:
				number = 1
			
		sum = sum + number
		dealer_sum=sum
		
	return dealer_sum
	

def dealer_hit(sum):
	number=0
	while True:
		if sum <=21:
			dealer_cards.append(card_deck.pop(0))
			number = dealer_cards[(len(dealer_cards))-1][0]
			if number == "J":
				number = 10
			elif number == "Q":
				number = 10
			elif number == "K":
				number = 10
			elif number == "A":
				if sum + 11 <= 21:
					number = 11
				else:
					number = 1
			
			sum= sum + number
			if sum > 21:
				card_deck.insert(0, dealer_cards.pop(-1))
			
				sum= sum - number
				break
			
		else:
			break
	
		
	
	dealer_sum = sum
	return dealer_sum	
		

def hit_me(sum):
	number = 0
	while True:
		if sum <= 21:
			hit=input("Do you want to hit or stay?\nPress 'y' to hit or 'n' to stay. ")
			if hit == "y":
				print('\n')
				delt_cards.append(card_deck.pop(0))
				print("Your cards:")
				print(delt_cards)
				number = delt_cards[(len(delt_cards))-1][0]
				if number == "J":
					number = 10
				elif number == "Q":
					number = 10
				elif number == "K":
					number = 10
				elif number == "A":
					while True:	
						a = input("What amount do yo want A to be? 1 or 11?\n")
						print()
						if a == "1":
							number = 1
							break
							
						elif a == "11":
							number = 11
							break
							
						else:
							print('Please enter a "1" or or a "11".')

			else:
				print("!" *2000)
				print()
				print ("Okay. Stand...")
				print()
				break
			
			sum = sum + number
			print()
			print(f"Your card sum is {sum}.")
			print()
			
		else:
			print("*" * 2000)
			print()
			print("You Bust!!!")
			print()
			break
		
			
	player_sum=sum
	return player_sum



cash = cash()
get_shuffle_cards()
while play == "y":
	get_dealer_cards()
	print("_" * 100)
	print("The dealers card shown:")
	print (dealer_cards[0],["??","???"])
	print()
	
	get_player_cards()
	print("Your cards:")
	print(delt_cards)
	
	player_sum = get_player_number(sum)
	print(f"Your card sum is {player_sum}.")
	print()
	player_sum = hit_me(player_sum)
	
	

	dealer_sum = get_dealer_number(sum)
	dealer_sum = dealer_hit(dealer_sum)	
	print("*" * 100)
	print("Dealer card results:")
	print (dealer_cards)
	print(f"Dealer sum is {dealer_sum}.")
	print()

	print("Your cards:")
	print(delt_cards)
	print(f"Your card sum is {player_sum}.")
	print()
	if player_sum > 21:
		cash = cash -10
		print(f"You lost $10. You cash amount is ${cash}.")
		
	elif dealer_sum > player_sum:
		cash = cash -10
		print (f"Dealer cards amount of {dealer_sum} greater than your card amount of {player_sum}. You lost $10 from round!!! You cash amount is ${cash}.")
	elif dealer_sum < player_sum:
		cash = cash + 10
		print (f"Dealer cards amount of {dealer_sum} less than your card amount of {player_sum}. You won $10 from round!!! Your cash amount is ${cash}.")
	elif dealer_sum == player_sum:
		print(f"It's a tie. Your cash amount is ${cash}.")


	print()
#Not recalling 237-248 not sure why not....
	if cash < 0:
		print(f"Tewst {cash}.")
		while cash<0:
			
			print("You need more cash..")
			cash = cash()
			
	if len(card_deck) <5:
			get_shuffle_cards()

	
			
	y = input("Do you want to play again? ")
	if y != "y":
		print(f"take home is ${cash}.")
		break
	else: 	
		delt_cards=[]
	#This is cards to dealer from deck.
		dealer_cards = []
	#Player sum of cards
		player_sum=0
	#dealer sum of cards
		daler_sum = 0
		sum=0