class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def findRow(self, matrix: List[List[int]], target: int) -> List[int]:
            left, right = 0, len(matrix) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if target < matrix[mid][0]:
                    right = mid - 1
                elif target > matrix[mid][-1]:
                    left = mid + 1
                else: return matrix[mid]

            return []

        def findTarget(self, row: List[int], target: int) -> bool:
            left, right = 0, len(row) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if target < row[mid]:
                    right = mid - 1
                elif target > row[mid]:
                    left = mid + 1
                else: return True
            return False

        row = findRow(self, matrix, target)

        if not row: return False

        return findTarget(self, row, target)