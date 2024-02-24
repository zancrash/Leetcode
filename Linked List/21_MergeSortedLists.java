class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode merged = new ListNode();
        ListNode head = merged;

        while (list1 != null && list2 != null)
        {
            if (list1.val < list2.val)
            {
                merged.next = list1;
                list1 = list1.next;
            }
            else
            {
                merged.next = list2;
                list2 = list2.next;
            }
            merged = merged.next;
        }

        if (list1 != null)
        {
            merged.next = list1;
        } 
        else if (list2 != null)
        {
            merged.next = list2;
        }

        return head.next;
    }
}