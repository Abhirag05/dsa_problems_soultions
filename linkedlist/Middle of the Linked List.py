# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast=slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
    
#Approach:Used "Tortoise and Hare Algorithm" which is by setting two pointers as slow and fast where the fast moves two nodes at a time whilw slow moves one.when the fast reaches the end the slow will be properly reached on the middle node

#Time Complexity: O(n) where n is the number of nodes in the linked list. The fast pointer traverses the list only once.

#Space Complexity:O(1) because we are only using two pointers (slow and fast) which take constant extra space regardless of the list size.