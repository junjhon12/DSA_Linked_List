class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def get_last(head):
  if not head: return None
  while head.next:
    head = head.next
  return head  

jigglypuff = Node("Jigglypuff")
wigglytuff = Node("Wigglytuff")
jigglypuff.next = wigglytuff

print(get_last(jigglypuff).value)