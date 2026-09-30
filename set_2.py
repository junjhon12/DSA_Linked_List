'Problem 1: Card Class'
class Card():
	def  __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
  
answer = Card("Spades", 8)
#print(answer.suit, answer.rank)

'Problem 2: Print Card'
class Card():
  def  __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank

  def print_card(self):
    print(f"{self.rank} of {self.suit}")

#answer = Card("Clubs", "Ace")
#answer.print_card()

'Problem 3: Verify Update'
class Card():
  def  __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank

  def print_card(self):
    print(f"{self.rank} of {self.suit}")

#answer = Card("Clubs", "Ace")
#answer.print_card()
#answer.suit = "Hearts"
#answer.print_card()

'Problem 4: Valid Card'
class Card():
  def  __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank

  def print_card(self):
    print(f"{self.rank} of {self.suit}")
    
  def is_valid(self):
    suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
    rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    
    if self.suit not in suits or self.rank not in rank: return False
    return True

my_card = Card("Hearts", "7")
#print(my_card.is_valid())

second_draw = Card("Spades", "Joker")
#print(second_draw.is_valid())

'Problem 5: Get Value'
class Card():
  def  __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank

  def print_card(self):
    print(f"{self.rank} of {self.suit}")
    
  def is_valid(self):
    suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
    rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    if self.suit not in suits or self.rank not in rank: return False
    return True
  
  def get_value(self):
    ranks = {"Ace": 1, "Jack": 11, "Queen": 12, "King": 13}
    if self.rank in [str(n) for n in range(2, 11)]:
      return self.rank
    if self.rank in ranks:
        return ranks[self.rank]
    return None

card = Card("Hearts", "7")
#print(card.get_value())

card_two = Card("Spades", "Jack")
#print(card_two.get_value())

'Problem 6: Hand Class'
class Hand:
  def __init__(self):
      self.cards = []
    
  def add_card(self, card):
    pass
    
  def remove_card(self, card):
    pass