import data_structures.linked_list as LL

llA = LL.LinkedList()
llB = LL.LinkedList()


node1 = LL.Node(8)
node2 = LL.Node(4)
node3 = LL.Node(5)

llA.insert_at_end(LL.Node(4))
llA.insert_at_end(LL.Node(1))
llA.insert_at_end(node1)
llA.insert_at_end(node2)
llA.insert_at_end(node3)

llB.insert_at_end(LL.Node(5))
llB.insert_at_end(LL.Node(6))
llB.insert_at_end(LL.Node(1))
llB.insert_at_end(node1)
llB.insert_at_end(node2)
llB.insert_at_end(node3)

headA = llA.head
headB = llB.head

l1, l2 = headA, headB
while l1 != l2:
    l1 = l1.next if l1 else headB
    l2 = l2.next if l2 else headA
print(l1)
