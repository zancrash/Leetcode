# 206: Reverse Linked List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Recursive:

        #Base case: No head, or we're on the last node
        if not head or not head.next:
            return head

        newHead = self.reverseList(head.next) # Continue recursion until Base case reached
        head.next.next = head # Reverse pointer
        head.next = None # Detach pointer

        return newHead

        # Iterative:
        # current = head
        # prev = None

        # while current:
        #     temp = current.next
        #     current.next = prev
        #     prev = current
        #     current = temp
        
        # return prev