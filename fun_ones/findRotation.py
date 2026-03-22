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

'''
n//2 and n+1 //2 takes care of 'seeds'. how many seeds are there for the matrix.
The inner loop which swaps 4 are fixed and dependent on i and j.   Because of that symmetry, one seed from the top-left quadrant is enough to "find" the other three positions via the formula.
You never need to visit those other positions as seeds, they'd just re-do the same swap and undo it.
n//2 for rows : you only need the top half. The bottom half is already covered as the "other side" of each cycle.
(n+1)//2 for columns : for even n this is the same as n//2 (a square quarter). For odd n it rounds up by one to include the center column, because the center column's cycles don't have a mirror on the right hence they fold back on themselve
