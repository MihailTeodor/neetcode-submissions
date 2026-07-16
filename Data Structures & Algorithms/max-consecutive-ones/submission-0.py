class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_count = 0
        for n in nums:
            if n == 1:
                count += 1
                if count >= max_count:
                    max_count = count
            else:
                count = 0

        return max_count