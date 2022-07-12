# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        stack = list()
        self.head = None 
        self.tail = None

        while head != None: 
            stack.append(head.val)
            head = head.next 

        print(stack)
        while stack: 
            val = stack.pop()
            new_node = ListNode(val)
            if self.head == None and self.tail == None: 
                self.head = new_node
                self.tail = new_node 
                continue

            self.tail.next = new_node 
            self.tail = self.tail.next

        return self.head


        
        
            
        
        