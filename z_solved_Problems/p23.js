function print(object) {
    console.log(object)
}
function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}

var l1 = new ListNode(1)
var l2 = new ListNode(4)
l1.next = l2
var l3 = new ListNode(5)
l2.next = l3


var m1 = new ListNode(1)
var m2 = new ListNode(3)
m1.next = m2
var m3 = new ListNode(4)
m2.next = m3

var n1 = new ListNode(2)
var n2 = new ListNode(6)
n1.next = n2

var lists = [l1, m1, n1]
var vals = []


for (let i = 0; i < lists.length; i++) {
    var curNode = lists[i]
    while (curNode != null) {
        print(curNode.val)
        vals.push(curNode.val)
        curNode = curNode.next
    }
}

vals.sort((a, b) => a - b)

var ans = new ListNode(0)
var cNode = ans
for (let i = 0; i < vals.length; i++) {
    cNode.next = new ListNode(vals[i])
    cNode = cNode.next
}


return ans