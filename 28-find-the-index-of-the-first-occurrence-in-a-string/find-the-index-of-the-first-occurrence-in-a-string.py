class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        idx=-1
        window=len(needle)
        for i in range(len(haystack)-window+1):
            if haystack[i:i+window]==needle:
                idx=i
                break
        return idx