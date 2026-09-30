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
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"


class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        if card in self.cards:
            self.cards.remove(card)

    def __repr__(self):
        return f"Hand({self.cards})"
    
  
card_one = Card("Hearts", "3")
card_two = Card("Spades", "8")

#player1_hand = Hand()
# cards = []
#player1_hand.add_card(card_one)
# cards = [card_one]
#player1_hand.add_card(card_two)
# cards = [card_one, card_two]
#player1_hand.remove_card(card_one)
# cards = [card_two]
#print(player1_hand)

'Problem 7: Sum of Cards'

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
      return int(self.rank)
    if self.rank in ranks:
        return ranks[self.rank]
    return None


class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        if card in self.cards:
            self.cards.remove(card)

    def __repr__(self):
        return f"Hand({self.cards})"
      
def sum_hand(hand):
  total = 0
  for card in hand.cards:
    if not card.is_valid():
      return None
    total += card.get_value()
  return total
      
  
card_one = Card("Hearts", "3")
card_two = Card("Hearts", "Jack")
card_three = Card("Spades", "3")

hand = Hand()
hand.add_card(card_one)
hand.add_card(card_two)
hand.add_card(card_three)

sum = sum_hand(hand)
#print(sum)

'Problem 8: Print Hand'

class Card:
    def __init__(self, suit, rank, next=None):
        self.suit = suit
        self.rank = rank
        self.next = next

    def __repr__(self):
        return f"{self.rank} of {self.suit}"


def print_hand(starting_card):
    hand = []
    current = starting_card
    while current is not None:
        hand.append(current)
        current = current.next
    print(hand)

card_one = Card("Hearts", "3")
card_two = Card("Hearts", "4")
card_three = Card("Diamonds", "King")

card_one.next = card_two
card_two.next = card_three

#print_hand(card_one)

'Problem 9: Head and Tail Nodes'

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

head = Node("199")
tail = Node("200")

head.next = tail

#print(head.value) 
#print(head.next.value) 
#print(tail.value) 
#print(tail.next) 

'Problem 10: Middle Node'

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
  
head = Node("199")
middle = Node("150")
tail = Node("200")

head.next = middle
middle.next = tail

#print(head.next.value) 
#print(middle.next.value)
#print(tail.next) 

'Problem 11: Zodiac Signs'

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

node_1 = Node("aries")
node_2 = Node("taurus")
node_3 = Node("gemini")
node_4 = Node("cancer")

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4

#print(node_1.value, "->", node_1.next.value)
#print(node_2.value, "->", node_2.next.value)
#print(node_3.value, "->", node_3.next.value)
#print(node_4.value, "->", node_4.next)

'Problem 12: Print Linked List'

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next= next
		
def print_linked_list(head):
  current = head
  while current is not None:
    if current.next is not None:
      print(current.value, end=" -> ")
    else:
      print(current.value)
    current = current.next

e = Node("e")
d = Node("d", e)
c = Node("c", d)
b = Node("b", c)
a = Node("a", b)
print_linked_list(a)