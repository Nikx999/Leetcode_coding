class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        new_head = None
        flag = 0
        prev = None
        while(head and head.next):
            print(head.val)
            
            temp = head
            head = head.next
            temp.next = head.next
            head.next = temp
            if flag != 0:
                prev.next = head
            print(temp.val,head.val)
            if flag==0: 
                new_head = head
                flag+=1
            prev = head.next
            head = head.next.next
            
            
        if flag==0:
            return head
        else:
            return new_head
