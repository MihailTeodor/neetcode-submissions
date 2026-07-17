class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1
        k = 0

        while left < right:
            while nums[left] != val and left < right:
                k += 1
                left += 1

            while nums[right] == val and left < right:
                right -= 1

            if left < right:
                k += 1
                nums[left] = nums[right]
                left += 1
                right -= 1

        if left == right and nums[left] != val:
            k += 1

        return k
            