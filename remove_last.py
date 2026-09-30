class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def remove_last(head):
  if not head or not head.next: return None
  current = head
  while current.next.next:
    current = current.next
  current.next = None
  return head


node_1 = Node("Jigglypuff")
node_1.next = Node("Wigglytuff")
node_1.next.next = Node("Ditto")

print(node_1.value, "->", node_1.next.value, "->", node_1.next.next.value)

node_1 = remove_last(node_1)
print(node_1.value, "->", node_1.next.value)

single = Node("Mew")
print(remove_last(single))