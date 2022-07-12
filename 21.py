# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
        
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        self.list1 = list1 
        self.list2 = list2 
        self.list3 = None
        self.tail = None
        
        while list1 != None and list2 != None: 
            
            val = 0
            if list1.val > list2.val: 
                val = list2.val
                list2 = list2.next
            else: 
                val = list1.val
                list1 = list1.next
            

            new_node = ListNode(val)
            if not self.list3: 
                self.list3 = new_node
                self.tail = new_node
            else: 
                self.tail.next = new_node
                self.tail = self.tail.next

        while list2 != None: 
            val = list2.val
            new_node = ListNode(val)
            if not self.list3: 
                self.list3 = new_node
                self.tail = new_node
            else: 
                self.tail.next = new_node
                self.tail = self.tail.next
            list2 = list2.next

        while list1 != None: 
            val = list1.val
            new_node = ListNode(val)
            if not self.list3: 
                self.list3 = new_node
                self.tail = new_node
            else: 
                self.tail.next = new_node
                self.tail = self.tail.next
            list1 = list1.next
            

        return self.list3

            
        print(self.list1.val)
        