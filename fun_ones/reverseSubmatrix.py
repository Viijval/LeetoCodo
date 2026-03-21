class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        output = [row[:] for row in grid]

        for i in range(k // 2):
            top_row = x + i
            bottom_row = x + k - 1 - i
            for j in range(y, y + k):
                output[top_row][j], output[bottom_row][j] = output[bottom_row][j], output[top_row][j]
        return output
