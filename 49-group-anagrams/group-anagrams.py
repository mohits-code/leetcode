class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        words=dict()
        for s in strs:
            val="".join(sorted(s))
            if val not in words:
                words[val]=[s]
                continue
            words[val].append(s)
        return words.values()

            
        