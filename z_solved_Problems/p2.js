function print(object) {
    console.log(object)
}
class ListNode {
    constructor(val) {
        this.val = val
        this.next = null
    }
}

var l1 = new ListNode(0)
var head1 = new ListNode(1)
l1.next = head1
var head2 = new ListNode(2)
head1.next = head2
var head3 = new ListNode(3)
head2.next = head3
var head4 = new ListNode(4)
head3.next = head4
var head5 = new ListNode(5)
head4.next = head5

var l2 = new ListNode(0)
var nums1 = new ListNode(1)
l2.next = nums1
var nums2 = new ListNode(9)
nums1.next = nums2
var nums3 = new ListNode(4)
nums2.next = nums3

var curHead = l1
var curnums = l2

var ansHead = new ListNode(0)
var ansCur = ansHead

var carry = 0

while ((curHead !== null || curnums !== null)) {
    var f = 0
    var s = 0
    if (curHead != null) {
        f = curHead.val
        curHead = curHead.next
    }
    if (curnums != null) {
        s = curnums.val
        curnums = curnums.next
    }

    var sum = f + s + carry
    if (sum >= 10) {
        carry = 1
        sum -= 10
    }
    else {
        carry = 0
    }
    ansCur.next = new ListNode(sum)
    ansCur = ansCur.next
    print(`${f} | ${s} | ${carry} | ${sum}`);

}
if (carry == 1) {
    ansCur.next = new ListNode(1)
    ansCur = ansCur.next
}

return ansHead.next