function print(object) {
    console.log(object)
}
class ListNode {
    constructor(val) {
        this.val = val
        this.next = null
    }
}

var head = new ListNode(1)
var node2 = new ListNode(2)
head.next = node2

var list = []
curNode = head
while (curNode != null) {
    list.push(curNode.val)
    curNode = curNode.next
}
var ansHeadNode = new ListNode(0)
var ansCurNode = ansHeadNode
for (let i = list.length - 1; i >= 0; i--) {
    ansCurNode.next = new ListNode(list[i])
    ansCurNode = ansCurNode.next
}
return ansHeadNode.next