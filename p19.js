function print(object) {
    console.log(object);
}

function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}

var head = new ListNode(1)
var head2 = new ListNode(2)
head.next = head2

//--------------------------- Ans ------------------------------------

var ans = new ListNode(0)
    var i = 1
    var len = 0

    cur = head
    ansCur = ans

    if (cur.next == null && n == 1) {
        i = 1;
    }
    while (cur != null) {
        len++
        cur = cur.next
    }

    cur = head
    n = len - (n - 1)

    while (cur != null) {
        if (i != n) {
            ansCur.next = new ListNode(cur.val)
            ansCur = ansCur.next
        }
        cur = cur.next
        i++
    }
    return ans.next