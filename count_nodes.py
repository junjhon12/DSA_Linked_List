class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def count_nodes(head):
  count = 0
  while head:
    count += 1
    head = head.next
  return count
  
jigglypuff = Node("Jigglypuff")
wigglytuff = Node("Wigglytuff")
ditto = Node("Ditto")
jigglypuff.next = wigglytuff
wigglytuff.next = ditto

print(count_nodes(jigglypuff))
print(count_nodes(None))