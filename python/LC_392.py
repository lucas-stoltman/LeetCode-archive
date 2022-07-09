# 392. Is Subsequence
# https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, target: str, input_string: str) -> bool:
        # search for each letter of word1 within word2
        # resume searching starting from that index spot

        ptr = 0
        temp = ""

        for i in range(len(target)):
            for j in range(ptr, len(input_string)):
                if target[i] == input_string[j]:
                    ptr = j
                    break
                elif j == len(input_string):
                    return False

        return temp == target

        # ptr1 = None
        # temp = ""
        #
        # # case 1
        # # iterate until it finds the matching letter
        # for i in range(len(t)):
        #     if s[0] == t[i]:
        #         ptr1 = i+1
        #         temp += t[i]
        #         break
        #     # if letter is not found by the end
        #     elif i == len(t) - 1:
        #         return False
        #
        # # case 2
        # # look for the rest of the letters from s
        # for i in range(1, len(s)):
        #     # iterate again, starting from the index of the last letter found
        #     # check each letter of input string
        #     for j in range(ptr1, len(t)):
        #         # check if the letter is found
        #         if s[i] == t[j]:
        #             ptr1 = j
        #             temp += t[j]
        #             break
        #         # if letter is not found by the end
        #         elif j == len(t) - 1:
        #             return False

        # return temp == s

    # ------------------------------------------------

    def test(self):
        sol = Solution()
        assert(sol.isSubsequence("abc", "xaxbxcx")) is True
        assert(sol.isSubsequence("acb", "abc")) is False
        assert(sol.isSubsequence("aaaaaa", "bbaaaa")) is False
        # assert (sol.isSubsequence("", "abc")) is True
        # assert (sol.isSubsequence("abc", "")) is False
        # print("All tests passed.")
