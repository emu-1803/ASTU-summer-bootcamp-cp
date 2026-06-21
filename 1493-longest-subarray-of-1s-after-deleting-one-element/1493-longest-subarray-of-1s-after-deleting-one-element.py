class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        left = 0
        zeros = 0
        max_len = 0
        for right in range(n):
            if nums[right] == 0:
                zeros += 1
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            size= (right - left) + 1
            size-=1
            max_len = max(max_len, size)
        return max_len