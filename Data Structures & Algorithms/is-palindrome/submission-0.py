class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ""
        reverse = ""
        for char in s:
            if char.isalnum():
                filtered += char.lower()
        for i in range(len(filtered) - 1, -1, -1):
            reverse += filtered[i]
        if reverse == filtered:
            return True
        return False
