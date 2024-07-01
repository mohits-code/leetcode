class Solution(object):
    def lengthOfLongestSubstring(self, s):
        '''q=[]
        m=0
        for char in s:
            if char in q:
                while char in q:
                    q.pop(0)
            q.append(char)
            print(q)
            m = max(m, len(q))

        return 
        
        '''
        cset= set()
        m=0
        l=len(s)
        left=0
        for right in range(l):
            while s[right] in cset:
                cset.remove(s[left])
                left+=1
            cset.add(s[right])
            m = max(m, right - left + 1)

        return m