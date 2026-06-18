class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        ans = 0
        l = 0

        while l < n:
            if nums[l] % 2 == 0 and nums[l] <= threshold:
                i = l
                while i + 1 < n and nums[i+1] <= threshold and nums[i] % 2 != nums[i+1] % 2:
                    i += 1
                ans = max(ans, i - l + 1)
                l = i + 1
            else:
                l += 1
        return ans

    