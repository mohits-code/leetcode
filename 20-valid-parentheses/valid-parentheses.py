class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        b = {')':'(', '}':'{', ']':'['}
        ob=[]
        for char in s:
            if char in b.values():
                ob.append(char)
            elif ob and b[char] == ob[-1]:
                ob.pop()
            else: return False
        return ob == []

        