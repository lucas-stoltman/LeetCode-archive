# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    from typing import Optional

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # iterate through list1 and compare each value with list2
        # add the smaller value to result []

        # refer to the first node we want to return
        prehead = ListNode(-1)

        prev = prehead
        # iterate through both linked lists
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next

        # add the rest of the longer list to the end
        prev.next = list1 or list2

        return prehead.next

    # ------------------------------------------------
    # TODO implement proper testing
    def test(self):
        sol = Solution()

        # list1
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(4)
        node1.next = node2
        node2.next = node3
        l1 = [node1, node2, node3]

        # list2
        node4 = ListNode(1)
        node5 = ListNode(3)
        node6 = ListNode(4)
        node4.next = node5
        node5.next = node6
        l2 = [node4, node5, node6]

        sol.mergeTwoLists(l1, l2)
        # assert (sol.isSubsequence("abc", "xaxbxcx")) is True
        # assert (sol.isSubsequence("acb", "abc")) is False
        # assert (sol.isSubsequence("aaaaaa", "bbaaaa")) is False
        # assert (sol.isSubsequence("", "abc")) is True
        # assert (sol.isSubsequence("abc", "")) is False
        # print("All tests passed.")
