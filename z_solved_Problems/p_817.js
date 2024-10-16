function print(object) {
    console.log(object)
}
class ListNode {
    constructor(val) {
        this.val = val
        this.next = null
    }
}

var head = new ListNode(0)
var head1 = new ListNode(1)
head.next = head1
var head2 = new ListNode(2)
head1.next = head2
var head3 = new ListNode(3)
head2.next = head3
var head4 = new ListNode(4)
head3.next = head4

var nums = new ListNode(0)
var nums1 = new ListNode(1)
nums.next = nums1
var nums2 = new ListNode(3)
nums1.next = nums2
var nums3 = new ListNode(4)
nums2.next = nums3

var curHead = head
var curnums = nums

var heads = []
var numss = []
var ans = 0

while (curHead != null) {
    heads.push(curHead.val)
    curHead = curHead.next

    if (curnums != null) {
        numss.push(curnums.val)
        curnums = curnums.next
    }
}
print(heads)
print(numss)

for (let i = 0; i < heads.length; i++) {
    if (numss.includes(heads[i])) {
        print(`includes ${heads[i]}`)
    }
    else {
        ans = heads[i]

    }

}
print(ans)