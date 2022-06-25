class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # if the characters map 1:1 then it is isomorphic
        current = 0
        first_word = []
        for i in range(len(s)-1):
            # if the next letter is different
            if s[i] != s[i+1]:
                current += 1
                # convert different letters into numbers to store
                first_word.append(current)

        current = 0
        second_word = []
        for i in range(len(t)-1):
            # convert letters into numbers to store
            # if the next letter is different
            if t[i] == t[i+1]:
                # increase current
                current += 1
                if current in second_word:
                    second_word_word.append(current)
                else:
                    second_word.append(current)

        # compare strings of numbers
        if first_word == second_word:
            return True
        else:
            return False


sol = Solution()
print(sol.isIsomorphic("foo", "bar"))


