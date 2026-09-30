class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def sum_list(head):
    sum = 0
    curr = head
    while curr is not None:
      # Add the value to the sum
      sum += curr.value
      curr = curr.next
    return sum
  
a = Node(5)
b = Node(10)
c = Node(15)
a.next = b
b.next = c

print(sum_list(a))
print(sum_list(None))