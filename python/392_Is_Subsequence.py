class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # search for each letter of s within t
        # assign the index to the letter in a dictionary
        # resume searching from that index spot

        word_dict = {}
        temp = ""

        # TODO fix "acb"

        # case 1
        # iterate until it finds the matching letter
        # if it reaches the end, return False
        for i in range(len(t)):
            if t[i] == s[0]:
                word_dict[t[i]] = i
                temp += t[i]
                print(t[i], i)
            # if letter is not found by the end
            elif i == len(t):
                return False

        # case 2
        # iterate again, starting from the index of the last letter found
        # if it reaches the end, return False
        for i in range(1, len(s)):
            j = 0
            # check each letter of input string
            for j in range(word_dict.get(t[j]), len(t)):
                # check if the letter is found
                if t[j] == s[i]:
                    word_dict[t[j]] = j
                    temp += t[j]
                    print(t[j], j)
                    break
                # if letter is not found by the end
                elif j == len(t):
                    return False
        print(temp, s)
        print(word_dict)
        return temp == s


# ------------------------------------------------


sol = Solution()
print(sol.isSubsequence("acb", "ahbgdc"))
