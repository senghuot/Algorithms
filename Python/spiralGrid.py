'''
Premise:
    given a two dimensional array, you need to print the array in a spiral format as follow.

Input:
    1    2   3   4
    5    6   7   8
    9   10  11  12
    13  14  15  16

Output:
    1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
'''

def spiralGrid(grid):
    top_index = 0
    bot_index = len(grid)-1
    lef_index = 0
    rig_index = len(grid[0])-1

    hori_offset = 0
    vert_offset = 1

    while top_index <= bot_index and rig_index >= lef_index:
        for i in range(hori_offset, len(grid[0])-hori_offset):
            print grid[top_index][i]

        for i in range(vert_offset, len(grid)-vert_offset):
            print grid[i][rig_index]

        for i in range(len(grid[0])-hori_offset-1, hori_offset-1, -1):
            print grid[bot_index][i]

        for i in range(len(grid)-vert_offset-1, vert_offset-1, -1):
            print grid[i][lef_index]

        top_index += 1
        bot_index -= 1
        lef_index += 1
        rig_index -= 1

        hori_offset += 1
        vert_offset += 1


grid = [[0,1,2,4], [5,6,7,8], [9,11,12,14], [15,16,17,18]]
spiralGrid(grid)