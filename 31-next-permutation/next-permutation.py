class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        pivot=-1

        i=len(nums)-2
        while i>=0:
            if nums[i]<nums[i+1]:
                pivot=i
                break
            i-=1
        
        if pivot==-1:
            nums.sort()
            return

        print(pivot)

        j=len(nums)-1
        while j>=pivot:
            if nums[j]>nums[pivot]:
                nums[pivot], nums[j]=nums[j],nums[pivot]
                break
            j-=1
        print(nums)
        l=pivot+1
        r=len(nums)-1

        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1