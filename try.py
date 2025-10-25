class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


lists = [2, 3, 4, 5, 6, 7]

head = None
tail = None

for i in lists:
    node = ListNode(i, None)
    if head is None:
        head = node
        tail = head
    else:
        tail.next = node
        tail = node

# sisipkan angka 8 diantara 4 dan 5
trav = head
while trav is not None:
    if trav.val == 4:
        new_node = ListNode(8, trav.next)
        trav.next = new_node
    trav = trav.next


# append new node di tail
tail.next = ListNode(10)

# append new head di depan
head = ListNode(100, head)

while head is not None:
    print(head.val)
    head = head.next


print(1 % 10)
