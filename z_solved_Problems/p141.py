import data_structures.linked_list as l

ll = l.LinkedList()

# ll.insert_values([3, 2, 0, -4])
ll.insert_at_begining(1)
ll.insert_at_begining(2)
# y = ll.insert_at_end(2)
# ll.insert_at_end(0)
# z = ll.insert_at_end(-4)
# z.next = y

if ll.get_length() == 1 and ll.head.next == None:
    print('false')
    

s = ll.head
f = ll.head

while f and f.next:
    s = s.next
    f = f.next.next
    if s == f:
        print('it is loop')
        break

print(f'{s} {f}')