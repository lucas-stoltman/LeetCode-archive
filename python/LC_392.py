# 392. Is Subsequence
# https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # search for each letter of s within t
        # resume searching starting from that index spot

        ptr = 0
        temp = ""

        for i in range(len(s)):
            for j in range(ptr, len(t)):
                if s[i] == t[j]:
                    ptr = j
                    ptr += 1
                    temp += t[j]
                    break
                elif j == len(t):
                    return False

        return temp == s

    # ------------------------------------------------

    def test(self):
        sol = Solution()
        assert(sol.isSubsequence("abc", "xaxbxcx")) is True
        assert(sol.isSubsequence("acb", "abc")) is False
        assert(sol.isSubsequence("aaaaaa", "bbaaaa")) is False
        assert (sol.isSubsequence("", "abc")) is True
        assert (sol.isSubsequence("abc", "")) is False
        print("All tests passed.")
