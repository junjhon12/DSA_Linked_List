class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def add_last(head, new_node):
  if head is None: return new_node
  
  curr = head
  while curr.next is not None:
    curr = curr.next
  curr.next = new_node
  return head
  
node_1 = Node("Jigglypuff")
node_2 = Node("Wigglytuff")
node_1.next = node_2

print(node_1.value, "->", node_1.next.value)

node_1 = add_last(node_1, Node("Ditto"))

print(node_1.value, "->", node_1.next.value, "->", node_1.next.next.value)