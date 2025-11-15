class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        idx=len(digits)-1
        carry=1
        while idx>=0:
            curr=digits[idx]+carry
            digits[idx]=curr%10
            carry=curr//10
            if carry==0:
                break
            idx-=1
        if carry!=0:
            digits=[carry]+digits
        return digits
