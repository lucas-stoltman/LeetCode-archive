# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # create a new list by "popping" each value from the LL

        # TODO beginning edge case
        original_head = head
        new_head = None
        pre = head

        # TODO Middle case
        pre = None
        while head:
            # set last node as new first node
            if head.next is Null:
                head.next = pre
                new_head = head
            else:
                pre = head
                nex = head.next
                head.next = pre

        # TODO ending edge case
        # set first node to null
        original_head.next = NULL


        return new_head
# ------------------------------------------------
def test(self):
    # sol = Solution()
    # assert (sol.isSubsequence("abc", "xaxbxcx")) is True
    # print("All tests passed.")


