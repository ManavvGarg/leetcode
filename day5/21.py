from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # boundry test cases to check if list is empty or not
        if list1 == []:
            return list2
        elif list2 == []:
            return list1
        elif list1 == [] and list2 == []:
            return []

        # dummy node
        start = ListNode()
        # dummy node's tail. only one node so head(start) and tail(end) will be same
        end = start

        # while list1 and list2 is not null
        while list1 and list2:
            # if list1.val is less than list2.val
            if list1.val < list2.val:
                end.next = list1
                list1 = list1.next
            else:
                end.next = list2
                list2 = list2.next
            end = end.next
        
        # end case if one of the list becomes null in above, add the remaining to the res linked list
        if list1:
            end.next = list1
        elif list2:
            end.next = list2
        
        return start.next


        