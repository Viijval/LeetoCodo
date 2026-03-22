class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
       # four possible rotations
        for k in range(4):
            # Loop over the first half of rows (top half)
            for i in range(n // 2):
                # Loop over the first half of columns (left half)
                # (n+1)//2 ensures center is included for odd n
                for j in range((n + 1) // 2):
                    # Perform a 4-way swap of elements
                    # These 4 positions form a cycle during rotation:
                    # (i, j) → (j, n-1-i) → (n-1-i, n-1-j) → (n-1-j, i)
                    (
                        mat[i][j],                       # top
                        mat[n - 1 - j][i],               # left
                        mat[n - 1 - i][n - 1 - j],       # bottom
                        mat[j][n - 1 - i],               #right

                    ) = (
                        mat[n - 1 - j][i],               # left → top
                        mat[n - 1 - i][n - 1 - j],       # bottom → left
                        mat[j][n - 1 - i],               # right → bottom
                        mat[i][j],                       # top → right
                    )
            if mat == target:
                return True
        return False
