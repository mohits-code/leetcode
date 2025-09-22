class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        prefix=0
        for i in range(len(nums)):
            nums[i]+=prefix
            prefix=nums[i]
        
        self.arr=nums
        print(nums)
        


    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left==0:
            return self.arr[right]
        return self.arr[right]-self.arr[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)