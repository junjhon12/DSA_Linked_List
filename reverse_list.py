class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def reverse_list(head):
    current = head
    previous = None
    
    while current:
      next = current.next
      current.next = previous
      previous = current
      current = next
    return previous
  
node_1 = Node("Jigglypuff")
node_1.next = Node("Wigglytuff")
node_1.next.next = Node("Ditto")

print(node_1.value, "->", node_1.next.value, "->", node_1.next.next.value)

node_1 = reverse_list(node_1)
print(node_1.value, "->", node_1.next.value, "->", node_1.next.next.value)