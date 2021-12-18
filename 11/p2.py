"""
--- Part Two ---

It seems like the individual flashes aren't bright enough to navigate.
However, you might have a better option: the flashes seem to be
synchronizing!

In the example above, the first time all octopuses flash simultaneously
is step 195:

    After step 193:
    5877777777
    8877777777
    7777777777
    7777777777
    7777777777
    7777777777
    7777777777
    7777777777
    7777777777
    7777777777

    After step 194:
    6988888888
    9988888888
    8888888888
    8888888888
    8888888888
    8888888888
    8888888888
    8888888888
    8888888888
    8888888888

    After step 195:
    0000000000
    0000000000
    0000000000
    0000000000
    0000000000
    0000000000
    0000000000
    0000000000
    0000000000
    0000000000

If you can calculate the exact moments when the octopuses will all flash
simultaneously, you should be able to navigate through the cavern. What
is the first step during which all octopuses flash?
"""


def read_input(fd):
    grid = []
    for line in fd:
        grid.append([int(x) for x in line.strip()])
    return grid


def charge_nearby(grid, xrange, yrange):
    flashes = 0
    for x in xrange:
        if x < 0 or x > 9:
            continue
        for y in yrange:
            if y < 0 or y > 9:
                continue
            value = grid[x][y] + 1
            grid[x][y] = value
            if value == 10:
                flashes += 1 + charge_nearby(grid, range(x - 1, x + 2), range(y - 1, y + 2))
    return flashes


def reset_flashed(grid):
    for x in range(10):
        for y in range(10):
            value = grid[x][y]
            if value > 9:
                grid[x][y] = 0


def solve(grid):
    for day in range(1000):
        if charge_nearby(grid, range(10), range(10)) == 100:
            return day + 1
        reset_flashed(grid)


def main():
    with open('input.txt') as fd:
        print(solve(read_input(fd)))


if __name__ == '__main__':
    main()
