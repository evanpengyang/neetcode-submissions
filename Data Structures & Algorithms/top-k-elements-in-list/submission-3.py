class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent = {}
        answer = [[] for i in range(len(nums) + 1)]
        for i in range(len(nums)):
            frequent[nums[i]] = frequent.get(nums[i], 0) + 1
        for key, value in frequent.items():
            answer[value].append(key)

        res = []
        
        for i in range(len(answer) -1, 0, -1):
            for n in answer[i]:
                res.append(n)
                if len(res) == k:
                    return res