class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        res=[0]*len(nums)
        l=0
        r=len(nums)-1
        for i in range(len(nums)):
            if nums[i]<pivot:
                res[l]=nums[i]
                l+=1
            if nums[len(nums)-1-i]>pivot:
                res[r]=nums[len(nums)-1-i]
                r-=1
        while l<=r:
            res[l]=pivot
            l+=1
        return res