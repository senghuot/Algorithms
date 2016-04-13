'''
    Premise: given M x N grid, where both rows and columns are sorted. Find coordinate of an element.

    Grid:
        [15,20,40,85]
        [20,35,80,95]
        [30,55,95,105]
        [40,80,100,120]
        [50,85,105,125]
        [60,90,110,130]
        [70,95,115,135]

'''

def nestedBinarySearch(grid, i_low, i_high, j_low, j_high, n):

    i_mid = (i_low + i_high) / 2
    j_mid = (j_low + j_high) / 2

    if i_low > i_high or j_low > j_high: return -1

    if i_high - i_low == 1 and j_high - j_low == 1:
        if grid[i_low][j_low] == n: return (i_low, j_low)
        if grid[i_low][j_low+1] == n: return (i_low, j_low+1)
        if grid[i_low+1][j_low] == n: return (i_low+1, j_low)
        if grid[i_low+1][j_low+1] == n: return (i_low+1, j_low+1)
        return -1

    # upper left quadrant
    if grid[i_low][j_low] <= n and n <= grid[i_mid][j_mid]:
        res = nestedBinarySearch(grid, i_low, i_mid, j_low, j_mid, n)
        if res != -1: return res


    # upper right quadrant
    if grid[i_low][j_mid] <= n and n <= grid[i_mid][j_high]:
        res = nestedBinarySearch(grid, i_low, i_mid, j_mid, j_high, n)
        if res != -1: return res


    # lower left quadrant
    if grid[i_mid][j_low] <= n and n <= grid[i_high][j_mid]:
        res = nestedBinarySearch(grid, i_mid, i_high, j_low, j_mid, n)
        if res != -1: return res


    # lower right quadrant
    if grid[i_mid][j_mid] <= n and n <= grid[i_high][j_high]:
        res = nestedBinarySearch(grid, i_mid, i_high, j_mid, j_high, n)
        if res != -1: return res

    return -1


A = [[15,20,40,85],[20,35,80,95],[30,55,95,105],[40,80,100,120], [50, 85, 105, 125], [60, 90, 110, 130], [70,95,115,135]]
print nestedBinarySearch(A, 0, 6, 0, 3, 135)