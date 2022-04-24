# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def convert(self, l):
        num = 0
        cur = l
        i = 0
        while cur:
            num += cur.val * 10**i 
            cur = cur.next
            i += 1
        print(num)
        return num
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = self.convert(l1), self.convert(l2);
        n = n1 + n2;
        list_n = list(reversed(str(n)))
        
        answer = ListNode()
        cur= answer
        for i, n in enumerate(list_n):
            cur.val = n;
            if i == len(list_n) - 1:
                return answer
            cur.next = ListNode()
            cur = cur.next
        