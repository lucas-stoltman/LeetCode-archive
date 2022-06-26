class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # if the characters map 1:1 then it is isomorphic
        def convert(word: str):
            # beginning edge case
            current = 0
            word_numbers = [current]
            word_letters = [word[0]]

            # handles 1 through (len-1)
            for i in range(1, len(word)):
                # if the current letter is different from the last
                if word[i] != word[i-1]:
                    # if the letter is in the list already
                    if word[i] in word_letters:
                        # place the same index as the letter
                        index = word_letters.index(word[i])
                        word_numbers.append(index)
                    else:
                        # place the same index as the letter
                        current += 1
                        word_letters.append(word[i])
                        word_numbers.append(current)
                else:
                    word_numbers.append(current)

            # ending edge case
            # word_numbers = [current]
            # word_letters = [word[len(word)-1]]

            return word_numbers

        first_word = convert(s)
        second_word = convert(t)

        # compare strings of numbers
        if first_word == second_word:
            return True
        else:
            return False


# ------------------------------------------------
sol = Solution()
print(sol.isIsomorphic("cat", "tac"))


