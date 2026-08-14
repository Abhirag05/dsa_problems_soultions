# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        curr=head
        while curr.next!=None:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        return prev

#approach: We can reverse a linked list by iterating through the list and changing the next pointers of each node to point to the previous node. We maintain three pointers: prev (initially None), curr (initially head), and next_node (to store the next node). In each iteration, we update the next pointer of curr to point to prev, then move prev and curr one step forward.

#time complexity: O(n), where n is the number of nodes in the linked list. We need to traverse the entire list once.

#space complexity: O(1), as we are using a constant amount of extra space for the pointers.