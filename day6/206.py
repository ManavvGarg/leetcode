from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # init 2ptrs for this optimal approach. One set to None/Null and one set to head
        # these will be used to get each element from the LL and also to iterate through the LL
        prev, curr = None, head
        
        # while curr ( head ) is not equal to NULL we iterate. Basically till the end of the LL
        while curr:
            # temp var to store the rest of the nodes that were previously attached to the current head node
            temp = curr.next
            # set curr.next to prev, now in first case it will be set to NULL
            curr.next = prev
            # set prev to curr, shift the ptr to curr's position
            prev = curr
            # assign the rest of the nodes to curr to get the remaining elements to avoid losing access to those elements
            curr = temp
        
        return prev

