# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution(object):
#     def removeNthFromEnd(self, head, n):
#         """
#         :type head: ListNode
#         :type n: int
#         :rtype: ListNode
#         """
class Solution(object):
    # def removeNthFromEnd(self, head, n):
    #     # with O(n) space
    #     index = []
    #     pos = head
    #     while pos is not None:
    #         index.append(pos)
    #         pos = pos.next
    #     ls = len(index)
    #     if n == ls:
    #         if ls > 1:
    #             return index[1]
    #         else:
    #             return None
    #     else:
    #         index_pos = ls - n - 1
    #         index[index_pos].next = index[index_pos + 1].next
    #         return head


    def removeNthFromEnd(self, head, n):
        # https://leetcode.com/discuss/86721/o-n-solution-in-java
        #http://bangbingsyb.blogspot.com/2014/11/leetcode-remove-nth-node-from-end-of.html
        # 
        if head is None:
            return None
        slow = fast = head
        for i in range(n):
            fast = fast.next
        if fast is None:
            head = head.next
            return head
        while fast.next is not None:  # while not fast.next  does not work 
            fast = fast.next
            slow = slow.next
        curr = slow.next
        slow.next = curr.next
        return head
