# TODO solution
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # search for each letter of s within t
        # assign the index to the letter in a dictionary
        # resume searching from that index spot

        word_dict = {}
        temp = ""

        # check each letter of target string
        for i in range(len(s)):
            # check each letter of input string
            for j in range(len(t)):
                # check if the letter is found
                if t[j] == s[i]:
                    word_dict[t[j]] = j
                    temp += t[j]
                    # print(t[j], j)
            # if letter is not found
            # return False
        return temp == s

# ------------------------------------------------


sol = Solution()
print(sol.isSubsequence("abc", "ahbgdc"))
