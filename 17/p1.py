"""
--- Day 17: Trick Shot --- https://adventofcode.com/2021/day/17

You finally decode the Elves' message. HI, the message says. You
continue searching for the sleigh keys.

Ahead of you is what appears to be a large ocean trench. Could the keys
have fallen into it? You'd better send a probe to investigate.

The probe launcher on your submarine can fire the probe with any integer
velocity in the x (forward) and y (upward, or downward if negative)
directions. For example, an initial x,y velocity like 0,10 would fire
the probe straight up, while an initial velocity like 10,-1 would fire
the probe forward at a slight downward angle.

The probe's x,y position starts at 0,0. Then, it will follow some
trajectory by moving in steps. On each step, these changes occur in the
following order:

-   The probe's x position increases by its x velocity.
-   The probe's y position increases by its y velocity.
-   Due to drag, the probe's x velocity changes by 1 toward the value 0;
    that is, it decreases by 1 if it is greater than 0, increases by 1
    if it is less than 0, or does not change if it is already 0.
-   Due to gravity, the probe's y velocity decreases by 1.

For the probe to successfully make it into the trench, the probe must be
on some trajectory that causes it to be within a target area after any
step. The submarine computer has already calculated this target area
(your puzzle input). For example:

    target area: x=20..30, y=-10..-5

This target area means that you need to find initial x,y velocity values
such that after any step, the probe's x position is at least 20 and at
most 30, and the probe's y position is at least -10 and at most -5.

Given this target area, one initial velocity that causes the probe to be
within the target area after any step is 7,2:

    .............#....#............
    .......#..............#........
    ...............................
    S........................#.....
    ...............................
    ...............................
    ...........................#...
    ...............................
    ....................TTTTTTTTTTT
    ....................TTTTTTTTTTT
    ....................TTTTTTTT#TT
    ....................TTTTTTTTTTT
    ....................TTTTTTTTTTT
    ....................TTTTTTTTTTT

In this diagram, S is the probe's initial position, 0,0. The x
coordinate increases to the right, and the y coordinate increases
upward. In the bottom right, positions that are within the target area
are shown as T. After each step (until the target area is reached), the
position of the probe is marked with #. (The bottom-right # is both a
position the probe reaches and a position in the target area.)

Another initial velocity that causes the probe to be within the target
area after any step is 6,3:

    ...............#..#............
    ...........#........#..........
    ...............................
    ......#..............#.........
    ...............................
    ...............................
    S....................#.........
    ...............................
    ...............................
    ...............................
    .....................#.........
    ....................TTTTTTTTTTT
    ....................TTTTTTTTTTT
    ....................TTTTTTTTTTT
    ....................TTTTTTTTTTT
    ....................T#TTTTTTTTT
    ....................TTTTTTTTTTT

Another one is 9,0:

    S........#.....................
    .................#.............
    ...............................
    ........................#......
    ...............................
    ....................TTTTTTTTTTT
    ....................TTTTTTTTTT#
    ....................TTTTTTTTTTT
    ....................TTTTTTTTTTT
    ....................TTTTTTTTTTT
    ....................TTTTTTTTTTT

One initial velocity that doesn't cause the probe to be within the
target area after any step is 17,-4:

    S..............................................................
    ...............................................................
    ...............................................................
    ...............................................................
    .................#.............................................
    ....................TTTTTTTTTTT................................
    ....................TTTTTTTTTTT................................
    ....................TTTTTTTTTTT................................
    ....................TTTTTTTTTTT................................
    ....................TTTTTTTTTTT..#.............................
    ....................TTTTTTTTTTT................................
    ...............................................................
    ...............................................................
    ...............................................................
    ...............................................................
    ................................................#..............
    ...............................................................
    ...............................................................
    ...............................................................
    ...............................................................
    ...............................................................
    ...............................................................
    ..............................................................#

The probe appears to pass through the target area, but is never within
it after any step. Instead, it continues down and to the right - only
the first few steps are shown.

If you're going to fire a highly scientific probe out of a super cool
probe launcher, you might as well do it with style. How high can you
make the probe go while still reaching the target area?

In the above example, using an initial velocity of 6,9 is the best you
can do, causing the probe to reach a maximum y position of 45. (Any
higher initial y velocity causes the probe to overshoot the target area
entirely.)

Find the initial velocity that causes the probe to reach the highest y
position and still eventually be within the target area after any step.
What is the highest y position it reaches on this trajectory?
"""


class Target:
    def __init__(self, line):
        x, y = line.split(' ')[2:]
        x = [int(v) for v in x[2:-1].split('..')]
        y = [int(v) for v in y[2:].split('..')]
        self.min_x = x[0]
        self.max_x = x[1]
        self.min_y = y[0]
        self.max_y = y[1]

    def within(self, x: int, y: int) -> bool:
        return self.min_x <= x <= self.max_x and self.min_y <= y <= self.max_y

    def get_steps(self):
        return 2 * max(self.max_x, abs(self.min_y), abs(self.max_y))

    def generate_velocity(self) -> (int, int):
        y_start = min(self.min_y, self.max_y)
        y_end = max(abs(self.min_y), abs(self.max_y))
        for x in range(self.max_x + 1):
            for y in range(y_start, y_end):
                yield x, y


class Probe:
    def __init__(self, x_velocity: int = 0, y_velocity: int = 0):
        self.x = 0
        self.y = 0
        self.max_y = 0
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity

    def step(self):
        self.x += self.x_velocity
        self.y += self.y_velocity

        if self.y > self.max_y:
            self.max_y = self.y

        if self.x_velocity > 0:
            self.x_velocity -= 1
        self.y_velocity -= 1

    def within(self, target: Target) -> bool:
        return target.within(self.x, self.y)


def solve(target: Target) -> int:
    result = 0
    for x, y in target.generate_velocity():
        probe = Probe(x, y)
        for _ in range(target.get_steps()):
            probe.step()
            if probe.within(target):
                result = max(result, probe.max_y)
                break
    return result


def main():
    with open('input.txt') as fd:
        for line in map(str.strip, fd):
            target = Target(line)
            print(solve(target))


if __name__ == '__main__':
    main()
