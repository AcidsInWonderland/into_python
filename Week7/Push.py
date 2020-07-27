# Util
# Robyn Lesch
# 17 June 2020
# Mood: excited


def create_grid(grid):
    """" create a 4x4 grid of zeroes """
    for i in range(4):
        grid.append([0, 0, 0, 0])


def print_grid(grid):
    """" print out a 4x4 grid in 5-width columns within a box """

    print("+--------------------+")

    for i in range(4):
        print("|", end="")
        for j in range(4):
            if grid[i][j] != 0:
                print("{0:<5}".format(grid[i][j]), end="")
            else:
                print("     ", end="")
        print("|")

    print("+--------------------+")


def check_lost(grid):
    """" return True if there are no 0 values and there are no
        adjacent values that are equal; otherwise False """
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                return False
            if j < 3:
                if grid[i][j] == grid[i][ j +1]:
                    return False
            if i < 3:
                if grid[i][j] == grid[i +1][j]:
                    return False

    return True


def check_won(grid):
    """" return True if a value>=32 is found in the grid; otherwise False """
    for i in range(4):
        for j in range(4):
            if grid[i][j] >= 32:
                return True
    return False


def copy_grid(grid):
    """" return a copy of the given grid """
    grid_copy = [[], [], [], []]
    for i in range(4):
        for j in range(4):
            grid_copy[i].append(grid[i][j])
    return grid_copy


def grid_equal(grid1, grid2):
    """ check if 2 grids are equal - return boolean value """
    for i in range(4):
        for j in range(4):
            if grid1[i][j] != grid2[i][j]:
                return False
    return True

