# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # iterate through list1 and compare each value with list2
        # add the smaller value to result []

        result = []
        ptr1 = 0
        ptr2 = 0

        for i in range(len(list1)+len(list2)):
            if list1[ptr1] <= list2[ptr2]:
                result += list1[ptr1]
                ptr1 += 1
            else:
                result += list2[ptr2]
                ptr2 += 1

        return result



# ------------------------------------------------
def test(self):
    # sol = Solution()
    # assert (sol.isSubsequence("abc", "xaxbxcx")) is True
    # assert (sol.isSubsequence("acb", "abc")) is False
    # assert (sol.isSubsequence("aaaaaa", "bbaaaa")) is False
    # assert (sol.isSubsequence("", "abc")) is True
    # assert (sol.isSubsequence("abc", "")) is False
    # print("All tests passed.")


