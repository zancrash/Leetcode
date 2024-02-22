# 21. Merge Two Sorted Lists

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        head = merged = ListNode() # init empty Listnode, head acts as a sentinal/dummy node

        # traverse through both lists, add lesser value to merged list first
        while list1 and list2: 
            if list1.val < list2.val:
                merged.next = list1
                list1 = list1.next
            else:
                merged.next = list2
                list2 = list2.next
            merged = merged.next
        
        merged.next = list1 if list1 else list2 # add remaining values from either list 1 or list 2 to merged list

        return head.next # head.next will point to head of merged list