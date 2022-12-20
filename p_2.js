function print(object) {
    console.log(object)
}
class ListNode {
    constructor(val) {
        this.val = val
        this.next = null
    }
}

var node1l1 = new ListNode(2)
var nodel2 = new ListNode(4)
node1l1.next = nodel2
var nodel3 = new ListNode(3)
nodel2.next = nodel3

var node2l4 = new ListNode(5)
var nodel5 = new ListNode(6)
node2l4.next = nodel5
var nodel6 = new ListNode(4)
nodel5.next = nodel6

curNode1 = node1l1
curNode2 = node2l4
var num1String = ''
var num2String = ''
while (curNode1 != null) {
    num1String += curNode1.val
    curNode1 = curNode1.next
}
while (curNode2 != null) {
    num2String += curNode2.val
    curNode2 = curNode2.next
}

var ans = (parseInt(num1String) + parseInt(num2String)).toString()
var ansHeadNode = new ListNode(0)
var ansNode = ansHeadNode

for (let i = ans.length - 1; i >= 0; i--) {
    ansNode.next = new ListNode(parseInt(ans[i]))
    ansNode = ansNode.next
}
return ansHeadNode.next