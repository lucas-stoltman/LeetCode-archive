class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # if the characters map 1:1 then it is isomorphic
        def convert(word: str):
            current = 0
            word_numbers = []
            word_letters = []
            # handles 0 through (len-1)
            for i in range(len(s)-1):
                # if the next letter is different
                if s[i] != s[i+1]:
                    # if the letter is in the list already
                    if s[i+1] in word_letters:
                        # place the same index as the letter
                        index = word_letters.index(s[i+1])
                        word_numbers.append(index)
                    else:
                        # place the same index as the letter
                        current += 1
                        word_letters.append(s[i])
                        word_numbers.append(current)
                else:
                    current += 1
                    word_letters.append(s[i])
                    word_numbers.append(current)

            return word_numbers

        first_word = convert(s)
        second_word = convert(t)

        # compare strings of numbers
        if first_word == second_word:
            return True
        else:
            return False


sol = Solution()
print(sol.isIsomorphic("cat", ""))


