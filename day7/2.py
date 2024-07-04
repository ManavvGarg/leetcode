from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        curr = dummy

        # while l1 exists or l2 exists.
        # also carry cause edge case where there might only one node in each list and that upon addition gives a carry, 8+7=15
        while l1 or l2 or carry:
            # if l1 exists then take l1.val
            value1 = l1.val if l1 else 0
            # if l2 exists then take l2.val
            value2 = l2.val if l2 else 0

            # compute total val
            total = value1 + value2 + carry

            # calculate carry
            carry = total // 10
            # calculate one's place
            total = total % 10

            # create new node
            curr.next = ListNode(total)

            # update ptrs
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        

        return dummy.next

        

        


        
                
                
        