class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # if the characters map 1:1 then it is isomorphic
        current = 0
        first_word_numbers = [current]
        first_word_letters = [s[0]]
        i = 1
        # handles 1 through (len-1)
        for i in range(len(s)-1):
            # if the next letter is different
            if s[i] != s[i+1]:
                # if the letter is in the list already
                if s[i] in first_word_letters:
                    first_word_numbers.append(first_word_letters[i])
            else:
                current += 1
                first_word_letters.append(s[i])
                first_word_numbers.append(current)

        # compare strings of numbers
        if first_word == second_word:
            return True
        else:
            return False


sol = Solution()
print(sol.isIsomorphic("foodsafjbsad", "babasdf"))


