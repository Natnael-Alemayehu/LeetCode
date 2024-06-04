class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head, n):
    dummy = ListNode(val=0, next=head)
    left = dummy
    right = head
    while n > 0 and right:
        right = right.next
        n -= 1

    while right:
        right = right.next
        left = left.next

    left.next = left.next.next

    return dummy.next
