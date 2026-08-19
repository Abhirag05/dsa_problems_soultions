# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next=curr.next.next
            else:
                curr=curr.next
        return head


#Approach:
# 1. We will traverse the linked list using a pointer 'curr'.
# 2. If the current node's value is equal to the next node's value, we will skip the next node.
# 3. Otherwise, we will move the pointer to the next node.
# 4. We will continue this process until we reach the end of the linked list.

#time complexity: O(n), where n is the number of nodes in the linked list.

#space complexity: O(1), as we are using only a constant amount of extra space.