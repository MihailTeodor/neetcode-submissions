class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = res = 0

        for n in nums:
            count = count + 1 if n else 0
            res = max(count, res)

        return res