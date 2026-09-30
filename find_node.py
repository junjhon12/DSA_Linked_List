class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_node(head, target):
    if head is None: return None
    
    while head:
      if head.value == target:
        return head
      head = head.next
    return None
  
node_1 = Node("Jigglypuff")
node_1.next = Node("Wigglytuff")

found = find_node(node_1, "Wigglytuff")
print(found.value if found else None)

print(find_node(node_1, "Mew"))