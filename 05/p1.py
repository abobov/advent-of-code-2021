"""
--- Day 5: Hydrothermal Venture --- https://adventofcode.com/2021/day/5
You come across a field of hydrothermal vents on the ocean floor! These vents
constantly produce large, opaque clouds, so it would be best to avoid them if
possible.

They tend to form in lines; the submarine helpfully produces a list of nearby
lines of vents (your puzzle input) for you to review. For example:

0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where
x1,y1 are the coordinates of one end the line segment and x2,y2 are the
coordinates of the other end. These line segments include the points at both
ends. In other words:

An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.

So, the horizontal and vertical lines from the above list would produce the
following diagram:

.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....
In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9.
Each position is shown as the number of lines which cover that point or . if no
line covers that point. The top-left pair of 1s, for example, comes from 2,2 ->
2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9
-> 2,9.

To avoid the most dangerous areas, you need to determine the number of points
where at least two lines overlap. In the above example, this is anywhere in the
diagram with a 2 or larger - a total of 5 points.

Consider only horizontal and vertical lines. At how many points do at least two
lines overlap?
"""


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def is_simple_line(self):
        return self.x1 == self.x2 or self.y1 == self.y2

    def points(self):
        if self.x1 == self.x2:
            # horizontal
            for y in range(min(self.y1, self.y2), max(self.y1, self.y2) + 1):
                yield (self.x1, y)
        else:
            # vertical
            for x in range(min(self.x1, self.x2), max(self.x1, self.x2) + 1):
                yield (x, self.y1)

    def __str__(self):
        return f'[{self.x1} {self.y1}] - [{self.x2} {self.y2}] (simple? {self.is_simple_line()}) : points {list(self.points())}'

    def __repr__(self):
        return self.__str__()


class Grid:
    def __init__(self):
        self.data = {}
        self.x_max = 0
        self.y_max = 0

    def add_line(self, line):
        self.update_size(line)
        for x, y in line.points():
            if x in self.data:
                row = self.data[x]
            else:
                row = {}
                self.data[x] = row

            if y in row:
                row[y] += 1
            else:
                row[y] = 1

    def update_size(self, line):
        self.y_max = max([self.x_max, line.x1 + 1, line.x2 + 1])
        self.x_max = max([self.y_max, line.y1 + 1, line.y2 + 1])

    def get_cell_value(self, x, y):
        if x in self.data:
            row = self.data[x]
            if y in row:
                return row[y]
        return 0

    def __str__(self):
        r = ''
        for y in range(self.y_max):
            for x in range(self.x_max):
                value = self.get_cell_value(x, y)
                if value == 0:
                    r += '.'
                else:
                    r += str(value)
            r += '\n'
        return r

    def __repr__(self):
        return self.__str__()

    def get_number_of_overlaps(self):
        result = 0
        for y in range(self.y_max):
            for x in range(self.x_max):
                if self.get_cell_value(x, y) > 1:
                    result += 1
        return result


def main():
    with open('input.txt') as fd:
        grid = Grid()
        for line in fd:
            p1, _, p2 = line.strip().split()
            coordinates = [int(coord) for point in [p1, p2] for coord in point.split(',')]
            l = Line(*coordinates)
            if l.is_simple_line():
                grid.add_line(l)
        print(grid.get_number_of_overlaps())


if __name__ == '__main__':
    main()
