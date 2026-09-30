'Problem 1: Pokemon Class'
class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False
        
a_pokemon = Pokemon("Charizard", ["Fire", "Dragon"])
#print(a_pokemon.name)
#print(a_pokemon.types)

'Problem 2: Create Squirtle'
class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
        print({
            "name": self.name,   
            "types": self.types, 
            "is_caught": self.is_caught 
        })

#answer = Pokemon("Squirtle", ["Water"])
#answer.print_pokemon()

'Problem 3: Is Caught'
#answer = Pokemon("Squirtle", ["Water"])
#answer.is_caught = True
#answer.print_pokemon()

'Problem 4: Catch Pokemon'
class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
        print({
            "name": self.name,   
            "types": self.types, 
            "is_caught": self.is_caught 
        })
    
    def catch(self):
        self.is_caught = True

#my_pokemon = Pokemon("rattata", ["Normal"])
#my_pokemon.print_pokemon()

#my_pokemon.catch()
#my_pokemon.print_pokemon()

'Problem 5: Choose Pokemon'
class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
        print({
            "name": self.name,   
            "types": self.types, 
            "is_caught": self.is_caught 
        })
    
    def catch(self):
        self.is_caught = True
        
    def choose(self):
        if self.is_caught is True:
            print(f"{self.name} I choose you!")
        print(f"{self.name} is wild! Catch them if you can!")
        

#my_pokemon = Pokemon("rattata", ["Normal"])
#my_pokemon.print_pokemon()

#my_pokemon.choose()
#my_pokemon.catch()
#my_pokemon.choose()

'Problem 6: Add Pokemon Type'
class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
        print({
            "name": self.name,   
            "types": self.types, 
            "is_caught": self.is_caught 
        })
    
    def catch(self):
        self.is_caught = True
        
    def choose(self):
        if self.is_caught is True:
            print(f"{self.name} I choose you!")
        print(f"{self.name} is wild! Catch them if you can!")
    
    def add_type(self, new_type):
        self.types.append(new_type)
        
#jigglypuff = Pokemon("Jigglypuff", ["Normal"])
#jigglypuff.print_pokemon()

#jigglypuff.add_type("Fairy")
#jigglypuff.print_pokemon()

'Problem 7: Get Pokemon'
class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
        print({
            "name": self.name,   
            "types": self.types, 
            "is_caught": self.is_caught 
        })
    
    def catch(self):
        self.is_caught = True
        
    def choose(self):
        if self.is_caught is True:
            print(f"{self.name} I choose you!")
        print(f"{self.name} is wild! Catch them if you can!")
    
    def add_type(self, new_type):
        self.types.append(new_type)
        
    def __repr__(self):
        return self.name
        
def get_by_type(my_pokemon, pokemon_type):
    return [p for p in my_pokemon if pokemon_type in p.types]

#jigglypuff = Pokemon("Jigglypuff", ["Normal", "Fairy"])
#diglett = Pokemon("Diglett", ["Ground"])
#meowth = Pokemon("Meowth", ["Normal"])
#pidgeot = Pokemon("Pidgeot", ["Normal", "Flying"])
#blastoise = Pokemon("Blastoise", ["Water"])

#my_pokemon = [jigglypuff, diglett, meowth, pidgeot, blastoise]
#normal_pokemon = get_by_type(my_pokemon, "Normal")
#print(normal_pokemon)

'Problem 8: Pokemon Evolution'
class Pokemon:
    def  __init__(self, name, types, evolution = None):
        self.name = name
        self.types = types
        self.is_caught = False
        self.evolution = evolution
        
    def __repr__(self):
            return self.name
        
def get_evolutionary_line(starter_pokemon):
    line = []
    current = starter_pokemon
    while current is not None:
        line.append(current)
        current = current.evolution
    return line

#charizard = Pokemon("Charizard", ["fire", "flying"])
#charmeleon = Pokemon("Charmeleon", ["fire"], charizard)
#charmander = Pokemon("Charmander", ["fire"], charmeleon)

#charmander_list = get_evolutionary_line(charmander)
#print(charmander_list)

#charmeleon_list = get_evolutionary_line(charmeleon)
#print(charmeleon_list)

#charizard_list = get_evolutionary_line(charizard)
#print(charizard_list)

'Problem 9: Node Class'
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

node_one = Node("a")
node_two = Node("b")

#print(node_one.value) 
#print(node_one.next) 
#print(node_two.value)
#print(node_two.next) 

'Problem 10: Linking Nodes'
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

node_one = Node("a")
node_one.next = node_two
node_two = Node("b")

#print(node_one.value)
#print(node_one.next.value)
#print(node_two.value)

'Problem 11: Mario Party'
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

node_1 = Node("Mario")
node_2 = Node("Luigi")
node_3 = Node("Wario")
node_4 = Node("Toad")

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4

#print(node_1.value, "->", node_1.next.value)
#print(node_2.value, "->", node_2.next.value)
#print(node_3.value, "->", node_3.next.value)
#print(node_4.value, "->", node_4.next)

'Problem 12: Printing Linked List'
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