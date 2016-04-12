# coding=utf-8
'''
Premise:
    An MxN grid: for each grid point, there is a certain amount of money on it.
    A person: top-left corner => bottom-right corner. Move right or down.
    Optimal path? collect the maximum sum of money.

Let define:
    Total Step = M + N - 2 steps
    Right step = M - 1
    Down step = N - 1

Permutation:
    (M + N - 2) choose (M - 1)


if M=N => (M-1) choose (2*M -2)  == M^2 ?

*---------------------------------------------------------------------------*
* Run time of this should be O(n!) Without dynamical programming, can solve *
* under O(2^n) because each cell has 2 options to go to, 'left' or 'right'. *
*---------------------------------------------------------------------------*


Using dynamic programming
-------------------------
Let:
    1. OPT(i, j) be the max sum of money at (i, j) starting from (0, 0)
    2. Cost(i, j) be the cost at (i, j)

    Finally, OPT(i, j) := Cost(i, j) + Max(OPT(i, j-1), OPT(i-1, j))
'''

def getMaxSum(grid):
    cache = {}

    # let’s fill in our base cases to build up the solutions
    for i in range(0, len(grid)):
        cache[(i, -1)] = (0, "")

    for j in range(0, len(grid[0])):
        cache[(-1, j)] = (0, "")

    # now let’s build the cache
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            top  = cache[(i-1, j)]
            left = cache[(i, j-1)]

            if top[0] > left[0]:
                turn = top[1] + "D"
            else:
                turn = left[1] + "R"

            cache[(i,j)] = (grid[i][j] + max(top[0], left[0]), turn)


    return cache[(len(grid) - 1, len(grid[0]) - 1)][1][1:]


grid = [[1,1,2,4], [5,6,7,8], [1,1,10,11], [1,1,1,1]]

assert getMaxSum(grid) == "DRRDRD"