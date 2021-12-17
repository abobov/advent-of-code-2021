"""
--- Part Two ---
Unfortunately, considering only horizontal and vertical lines doesn't give you
the full picture; you need to also consider diagonal lines.

Because of the limits of the hydrothermal vent mapping system, the lines in your
list will only ever be horizontal, vertical, or a diagonal line at exactly 45
degrees. In other words:

An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.
Considering all lines from the above example would now produce the following
diagram:

1.1....11.
.111...2..
..2.1.111.
...1.2.2..
.112313211
...1.2....
..1...1...
.1.....1..
1.......1.
222111....
You still need to determine the number of points where at least two lines
overlap. In the above example, this is still anywhere in the diagram with a 2 or
larger - now a total of 12 points.

Consider all of the lines. At how many points do at least two lines overlap?
"""


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def points(self):
        x_step = -1 if self.x1 > self.x2 else 1
        y_step = -1 if self.y1 > self.y2 else 1
        if self.x1 == self.x2:
            # horizontal
            for y in range(min(self.y1, self.y2), max(self.y1, self.y2) + 1):
                yield self.x1, y
        elif self.y1 == self.y2:
            # vertical
            for x in range(min(self.x1, self.x2), max(self.x1, self.x2) + 1):
                yield x, self.y1
        else:
            distance = max(self.x1, self.x2) - min(self.x1, self.x2)
            for d in range(distance + 1):
                yield self.x1 + d * x_step, self.y1 + d * y_step

    def __str__(self):
        return f'[{self.x1} {self.y1}] - [{self.x2} {self.y2}] : points {list(self.points())}'

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
            grid.add_line(l)
        print(grid.get_number_of_overlaps())

if __name__ == '__main__':
    main()
