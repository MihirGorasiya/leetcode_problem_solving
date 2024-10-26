import data_structures.linked_list as ll

ll1 = ll.LinkedList()
ll1.insert_values([3, 2, 0])
ll1.print()
head = ll1.head
seen = set()

while head:
    if head not in seen:
        seen.add(head)
    else:
        print(head)
    head = head.next
