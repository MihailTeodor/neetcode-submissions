class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        right = len(nums)

        while k < right:
            if nums[k] == val:
                right -= 1
                nums[k] = nums[right]
            else:
                k += 1

        return k
            



            