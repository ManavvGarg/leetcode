from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        emptyList = []
        if lists==[] or lists==[[]]:
            return None
        sortedLL = ListNode()
        dummy = sortedLL

        for i in lists:
            while i:
                emptyList.append(i.val)
                i=i.next
        
        emptyList.sort()
        for i in emptyList:
            tmp = ListNode(i)
            dummy.next = tmp
            dummy = dummy.next
        
        return sortedLL.next
