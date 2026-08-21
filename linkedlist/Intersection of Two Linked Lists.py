# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen=set()
        curr1=headA
        curr2=headB
        while curr1:
            seen.add(curr1)
            curr1=curr1.next
        while curr2:
            if curr2 in seen:
                return curr2
            curr2=curr2.next
        return None

#Approach:
# 1. We will use a set to store the nodes of the first linked list (headA).
# 2. We will traverse the second linked list (headB) and check if any node is present in the set.
# 3. If we find a node in the set, we will return that node as the intersection point.
# 4. If we reach the end of the second linked list without finding any intersection, we will return None.

#time complexity: O(n + m), where n is the number of nodes in the first linked list and m is the number of nodes in the second linked list. We traverse both lists once.

#space complexity: O(n), where n is the number of nodes in the first linked list. We use a set to store the nodes of the first linked list.