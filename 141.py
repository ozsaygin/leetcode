

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        ptr = head
        self.nodes = { }
        
        while ptr != None: 

            if ptr.val not in self.nodes:

                self.nodes[ptr.val] = list()
                
            
            else: # if exist check whether node in its list

                if ptr in self.nodes[ptr.val]:
                    return True

            self.nodes[ptr.val].append(ptr)
            ptr = ptr.next

        return False