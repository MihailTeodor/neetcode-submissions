class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        newArray = [0] * (n * 2)

        for i in range(n):
            newArray[i] = newArray[i + n] = nums[i]
        
        return newArray