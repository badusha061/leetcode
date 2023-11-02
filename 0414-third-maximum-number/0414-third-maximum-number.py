class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n = set(nums)
        nums = list(n)
        nums.sort()
        if len(nums) >= 3:
            return nums[-3]
        else:
            return nums[-1]
        