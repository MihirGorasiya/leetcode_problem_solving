import data_structures.linked_list as l

ll = l.LinkedList()
ll.insert_values([1, 2, 3])
head = ll.head
k = 5

'''
1 2 3
3 1 2
2 3 1
'''


temp_head = head
length = 0
tail = None
while temp_head:
    length += 1
    tail = temp_head
    temp_head = temp_head.next

temp_head = head
tail.next = temp_head

for i in range(length - (k % length)):
    tail = tail.next

temp_head = tail.next
tail.next = None

while temp_head:
    
    temp_head = temp_head.next


# temp_head = head
# linked_list_length = 0
# while temp_head:
#     linked_list_length += 1
#     temp_head = temp_head.next
# temp_head = head
# second_last_element = None
# last_element = None

# for i in range(k % linked_list_length):
#     if last_element == None:
#         print("last element not set")
#         while temp_head.next:
#             second_last_element = temp_head
#             last_element = temp_head.next
#             temp_head = temp_head.next
#         print(f"last element is {last_element.data}")

#     temp_Node = second_last_element.next
#     second_last_element.next = None
#     temp_Node.next = head
#     head = temp_Node
#     last_element = None
#     print(i)
