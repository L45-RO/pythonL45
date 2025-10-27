class Solution(object):
    def removeNthFromEnd(self, head, n):

        # Step 0: create dummy node pointing to head
        dummy =ListNode(0,head)
        fast = dummy
        slow = dummy

        # Step 1: Move fast n+1 steps ahead
        for _ in range (n+1):
            fast = fast.next

        # Step 2: Move both pointers until fast reaches the end
        while fast:
            fast=fast.next
            slow=slow.next
        slow.next =slow.next.next

        # Step 4: Return new head
        return dummy.next