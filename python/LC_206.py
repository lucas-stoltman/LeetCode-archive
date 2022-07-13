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


        # TODO Middle case
        while head:
            temp = head.next
            pointer = head
            ListNode(-1)

        # TODO ending edge case

# ------------------------------------------------
def test(self):
    # sol = Solution()
    # assert (sol.isSubsequence("abc", "xaxbxcx")) is True
    # print("All tests passed.")


