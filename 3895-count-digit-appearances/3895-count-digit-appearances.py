class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        t=0
        dig = str(digit) 
        for i in range(len(nums)):
            num = str(nums[i])
            t += num.count(dig)
        return t