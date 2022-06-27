class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # if the characters map 1:1 then it is isomorphic
        def convert(word: str):
            # beginning edge case
            current = 0
            word_numbers = [current]
            stored_letters = [word[0]]

            # handles 1 through (len-1)
            for i in range(1, len(word)):
                current_letter = word[i]
                last_letter = word[i-1]

                # if the current letter is different from the last
                if current_letter not in last_letter:
                    # if the letter is in the list already
                    if current_letter in stored_letters:
                        index = stored_letters.index(current_letter)
                        # place the same index as the letter
                        word_numbers.append(index)
                    else:
                        # place the same index as the letter
                        current += 1
                        stored_letters.append(word[i])
                        word_numbers.append(current)
                else:
                    index = stored_letters.index(current_letter)
                    word_numbers.append(index)
            return word_numbers

        first_word = convert(s)
        second_word = convert(t)

        # compare strings of numbers
        return first_word == second_word


# ------------------------------------------------
sol = Solution()
print(sol.isIsomorphic("abbaa", "cddcd"))


