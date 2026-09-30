class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_len = len(matrix[0])
        column_len = len(matrix)

        t, b = 0, column_len - 1
        while t <= b:
            m = t + (b - t)//2
            if matrix[m][0] > target:
                b = m - 1
            elif matrix[m][-1] < target:
                t = m + 1
            else:
                break

        low, high = 0, row_len - 1

        while low <= high:
            mid = low + (high - low)//2
            if matrix[m][mid] == target:
                return True
            elif matrix[m][mid] < target:
                low = mid + 1
            elif  matrix[m][mid] > target:
                high = mid - 1
        return False
            