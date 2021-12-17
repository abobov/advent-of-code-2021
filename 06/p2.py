"""
--- Part Two ---
Suppose the lanternfish live forever and have unlimited food and space. Would
they take over the entire ocean?

After 256 days in the example above, there would be a total of 26984457539
lanternfish!

How many lanternfish would there be after 256 days?
"""
from functools import cache


@cache
def solve(fish, days):
    result = 1
    for day in range(days):
        if fish == 0:
            fish = 6
            result += solve(8, days - day - 1)
        else:
            fish -= 1
    return result


def main():
    days = 256
    with open('input.txt') as fd:
        fishes = [int(x) for x in fd.readline().strip().split(',')]
        print(sum([solve(fish, days) for fish in fishes]))


if __name__ == '__main__':
    main()
