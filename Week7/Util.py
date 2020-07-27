# Push
# Robyn Lesch
# 17 June 2020
# Mood: happy

def analyse(line):
    new = []
    for i in range(4):
        new.append(line[i])

    if len(new) == 4:
        if new[-2] == 0 and new[0] == new[1] and new[-1] != new[0] and new[-1] != 0:
            new[0] = 0
            new[2] = 2 * new[1]
            new[1] = 0
            return new

    while 0 in new:
        new.remove(0)
    for i in range(4):
        if len(new) > i:
            if new[-i] != 0:
                if i < len(new) - 1:
                    if new[-i - 1] == 0:
                        new[-i - 1] = new[-i]
                        new[-i] = 0
                        new.remove(0)
                    elif new[-i - 1] == new[-i - 2]:
                        new[-i - 1] = 2 * new[-i - 1]
                        new[-i - 2] = 0
                        new.remove(0)
        else:
            break
    new.reverse()
    for i in range(4 - len(new)):
        new.append(0)
    new.reverse()
    return new


def push_up(grid):
    """ merge grid values upwards """
    for i in range(4):
        new_line = analyse([grid[3][i], grid[2][i], grid[1][i], grid[0][i]])
        for j in range(4):
            grid[-j - 1][i] = new_line[j]


def push_down(grid):
    """ merge grid values downwards """
    for i in range(4):
        new_line = analyse([grid[0][i], grid[1][i], grid[2][i], grid[3][i]])
        for j in range(4):
            grid[j][i] = new_line[j]


def push_left(grid):
    """ merge grid values left """
    for i in range(4):
        new_line = analyse([grid[i][3], grid[i][2], grid[i][1], grid[i][0]])
        for j in range(4):
            grid[i][j] = new_line[-j - 1]


def push_right(grid):
    """ merge grid values right """
    for i in range(4):
        new_line = analyse([grid[i][0], grid[i][1], grid[i][2], grid[i][3]])
        for j in range(4):
            grid[i][j] = new_line[j]
