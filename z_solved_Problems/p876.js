function print(object) {
    console.log(object)
}
class ListNode {
    constructor(val) {
        this.val = val
        this.next = null
    }
}
class LinkedList {
    constructor(head = null) {
        this.head = head
    }
}
let node1 = new ListNode(2)
let node2 = new ListNode(3)
node1.next = node2
let node3 = new ListNode(4)
node2.next = node3
let node4 = new ListNode(5)
node3.next = node4
let node5 = new ListNode(6)
node4.next = node5
let node6 = new ListNode(7)
node5.next = node6

var curNode = node1
var length = 0
while (curNode != null) {
    length++
    curNode = curNode.next
}
curNode = node1
let headNode = new ListNode(0);
let currNode = headNode
for (let i = 1; i <= length; i++) {
    if (i > Math.floor(length / 2)) {
        currNode.next = new ListNode(curNode.val)
        currNode = currNode.next
    }

    curNode = curNode.next
}

return headNode.next
