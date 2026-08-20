# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """seen=set()
        curr=head
        while curr:
            if curr in seen:
                return True
            seen.add(curr)
            curr=curr.next
        return False"""

        fast=slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False

#Approach:
# 1. We will use two pointers, 'slow' and 'fast', both starting at the head of the linked list.
# 2. The 'slow' pointer will move one step at a time, while the 'fast' pointer will move two steps at a time.
# 3. If there is a cycle in the linked list, the 'fast' pointer will eventually meet the 'slow' pointer.
# 4. If the 'fast' pointer reaches the end of the linked list (ie., fast or fast.next is None), then there is no cycle in the linked list.

#time complexity: O(n), where n is the number of nodes in the linked list.

#space complexity: O(1), as we are using only a constant amount of extra space.