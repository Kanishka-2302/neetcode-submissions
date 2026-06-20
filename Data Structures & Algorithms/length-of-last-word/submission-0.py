class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last = ""
        for i in range(len(s)):
            if s[i] != " ":
                if i > 0 and s[i-1] == " ":
                    last = ""
                last+= s[i]
        return len(last)