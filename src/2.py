class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c = 0
        dummyHead = ListNode(0)
        curr = dummyHead
        while l1 != None or l2 != None:
            x = l1.val if l1 != None else 0
            y = l2.val if l2 != None else 0
            sum = x + y + c
            curr.next = ListNode(sum % 10)
            curr=curr.next
            if l1!=None:
                l1=l1.next
            if l2!=None:
                l2=l2.next
            c=sum/10
        else:
            if c!=0:
                curr.next=ListNode(c)   
        return dummyHead.next
    

            
            
