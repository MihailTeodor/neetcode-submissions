class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = [0] * 3

        for color in nums:
            buckets[color] += 1

        i = 0
        for j in range(3):
            for k in range(buckets[j]):
                nums[i] = j
                i += 1