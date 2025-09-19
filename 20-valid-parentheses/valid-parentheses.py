class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parenthesis={"(":")", "[":"]", "{":"}"}
        stack = []
        for char in s:
            if char in parenthesis.keys():
                stack.append(char)
            elif not stack:
                return False
            elif parenthesis[stack.pop()] != char:
                    return False
        if len(stack)!=0:
            return False
        return True