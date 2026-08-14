'''    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def insertAtEnd(self, head, x):
        #code here 
        new_node=Node(x)
        if not head:
            return new_node
        curr=head
        while curr.next!=None:
            curr=curr.next
        curr.next=new_node
        return head
            

#Approach: Create a new node with the given value x. If the linked list is empty (head is None), return the new node as the head. Otherwise, traverse the linked list to find the last node and set its next pointer to the new node.

#time complexity: O(n), where n is the number of nodes in the linked list. We need to traverse the entire list to find the last node.

#space complexity: O(1), as we are using a constant amount of extra space for the new node and pointers.