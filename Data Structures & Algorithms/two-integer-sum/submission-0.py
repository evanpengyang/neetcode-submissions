class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        two_sum = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in two_sum:
                return [two_sum[difference], i]
            two_sum[nums[i]] = i