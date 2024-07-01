class Solution(object):
    def lengthOfLongestSubstring(self, s):
        q=[]
        m=0
        for char in s:
            if char in q:
                while char in q:
                    q.pop(0)
            q.append(char)
            print(q)
            m = max(m, len(q))

        return m