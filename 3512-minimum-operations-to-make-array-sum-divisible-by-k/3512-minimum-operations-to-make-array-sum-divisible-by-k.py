class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        sums=sum(nums)
        ans=sums%k
        return ans