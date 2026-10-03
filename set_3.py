'Problem 1: Player Class'
class Player():
	def  __init__(self, character, kart):
		self.character = character
		self.kart = kart

answer = Player("Yoshi", "Super Blooper")
#print(answer.character, answer.kart)

'Problem 2: Get Player'
class Player():
     def  __init__(self, character, kart):
          self.character = character
          self.kart = kart

     def get_player(self):
          return f"{self.character} driving the {self.kart}"

player_two = Player("Browser", "Pirahna prowler")
player_one = Player("Yoshi", "Super Blooper")
#print(f'Match: {player_one.get_player()} vs {player_two.get_player()}')

'Problem 3: Update Kart'
class Player():
     def  __init__(self, character, kart):
          self.character = character
          self.kart = kart

     def get_player(self):
          return f"{self.character} driving the {self.kart}"
     
#print(player_one.get_player())
player_one.kart = "Dolphin Dasher"
#print(player_one.get_player())     

'Problem 4: Set Character'
class Player:
     def __init__(self, character, kart):
          self.character = character
          self.kart = kart
          self.items = []

     def set_player(self, name):
          valid_names = ["Mario", "Luigi", "Peach", "Yoshi", "Toad", "Wario", "Donkey Kong", "Bowser"]
          if name not in valid_names:
               return "Invalid character"
          self.character = name
          return "Character updated"

player_one = Player("Yoshi", "Super Blooper")
player_two = Player("Bowser", "Pirahna Prowler")

#print(player_one.set_player("Peach"))   
#print(player_two.set_player("Kermit"))   

'Problem 5: Add Special Item'
class Player():
	def  __init__(self, character, kart):
		self.character = character
		self.kart = kart
		self.items = []
		
	def add_item(self, item_name):
          self.items.append(item_name)
          print(self.items)

#player_one = Player("Yoshi", "Dolphin Dasher")
# items = []

#player_one.add_item("red shell")
# items = ["red shell"]

#player_one.add_item("super star")
# items = ["red shell", "super star"]

#player_one.add_item("super smash")
# items = ["red shell", "super star"]

'Problem 6: Print Inventory'
class Player():
     def  __init__(self, character, kart):
          self.character = character
          self.kart = kart
          self.items = []

     def print_inventory(self):
          if not self.items:
               print("Inventory empty")
               return
          
          counts = {}
          for item in self.items:
               counts[item] = counts.get(item, 0) + 1
          
          inventory_str = ", ".join(f'{item}: {count}' for item, count in counts.items())
          
          print(f"inventory: {inventory_str}")
     
player_one = Player("Yoshi", "Super Blooper")
player_one.items = ["banana", "bob-omb", "banana", "super star"]
player_two = Player("Peach", "Dolphin Dasher")

#player_one.print_inventory()
#player_two.print_inventory()

'Problem 7: Race Results'
class Player:
    def __init__(self, character, kart):
          self.character = character
          self.kart = kart
          self.items = []
        
def print_inventory(self):
     if not self.items:
          print("Inventory empty")
          return
     counts = {}
     for item in self.items:
          counts[item] = counts.get(item, 0) + 1
     inventory_str = ", ".join(f'{item}: {count}' for item, count in counts.items())
     print(f"inventory: {inventory_str}")
	
	
def print_results(race_results):
     for i, player in enumerate(race_results, start=1):
          print(f'{i}. {player.character}')

peach = Player("Peach", "Daytripper")
mario = Player("Mario", "Standard Kart M")
luigi = Player("Luigi", "Super Blooper")
race_one = [peach, mario, luigi]

print_results(race_one)