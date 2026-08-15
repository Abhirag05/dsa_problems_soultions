# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        curr=dummy
        while list1 and list2:
            if list1.val<=list2.val:
                curr.next=list1
                list1=list1.next
            else:
                curr.next=list2
                list2=list2.next
            curr=curr.next
        if list1:
            curr.next=list1
        else:
            curr.next=list2
        return dummy.next


#Approach: We can merge two sorted linked lists by iterating through both lists and comparing the values of the current nodes. We maintain a dummy node to simplify the merging process and a current pointer to build the merged list. In each iteration, we compare the values of the nodes from both lists and append the smaller one to the merged list. After one of the lists is exhausted, we append the remaining nodes from the other list.

#Time complexity: O(n + m), where n and m are the lengths of the two linked lists. We need to traverse both lists once.

#Space complexity: O(1), as we are using a constant amount of extra space for the pointers.