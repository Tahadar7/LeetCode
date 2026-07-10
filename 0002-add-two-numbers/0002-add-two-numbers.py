# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_values = []
        l2_values = []

        curr = l1
        while curr:
            l1_values.append(str(curr.val))
            curr = curr.next

        curr = l2
        while curr:
            l2_values.append(str(curr.val))
            curr = curr.next

        l1_values = l1_values[::-1]    #  reverse the order
        l2_values = l2_values[::-1]

        l1_num = int(''.join(l1_values))    # convert to int
        l2_num = int(''.join(l2_values))

        new_digits = str(l1_num + l2_num)[::-1]    # add both and reverse the order
        dummy = ListNode()

        curr = dummy
        for d in new_digits:
            curr.next = ListNode(int(d))   
            curr = curr.next
            
        return dummy.next   # first is empty

        