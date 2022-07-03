class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # search for each letter of s within t
        # assign the index to the letter in a dictionary
        # resume searching from that index spot

        word_dict = {}
        temp = ""

        # base case
        if s == "":
            return True

        # case 1
        # iterate until it finds the matching letter
        for i in range(len(t)):
            if t[i] == s[0]:
                word_dict[t[i]] = i
                temp += t[i]
                break
            # if letter is not found by the end
            elif i == len(t)-1:
                return False

        # case 2
        # look for the rest of the letters from s
        j = 0
        for i in range(1, len(s)):
            # iterate again, starting from the index of the last letter found
            # check each letter of input string
            for j in range(word_dict.get(t[j]), len(t)):
                # check if the letter is found
                if t[j] == s[i]:
                    word_dict[t[j]] = j
                    temp += t[j]
                    # print(t[j], j)
                    break
                # if letter is not found by the end
                elif j == len(t)-1:
                    return False
        # print(temp, s)
        # print(word_dict)
        return temp == s


# ------------------------------------------------


sol = Solution()
print(sol.isSubsequence("abc", "ahbdc"))
