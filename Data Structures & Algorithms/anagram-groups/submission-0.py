class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letters = {}

        for words in strs:
            key = "".join(sorted(words))
            if key not in letters:
                letters[key] = []
            letters[key].append(words)

        return list(letters.values())