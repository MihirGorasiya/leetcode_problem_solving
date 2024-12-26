import data_structures.linked_list as l

head = [1, 2, 3,4]
ll = l.LinkedList()
ll.insert_values(head)
head = ll.head
ans = head.next
prev = None
while head:
    if not head.next:
        break
    temp = head.next
    head.next = temp.next
    temp.next = head
    if prev:
        prev.next = temp
    prev = temp.next
    head = head.next

print('-------------------')

while ans:
    print(ans.data)
    ans = ans.next
# llAnsHead.next.print()