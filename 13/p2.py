"""
--- Part Two ---
Finish folding the transparent paper according to the instructions.
The manual says the code is always eight capital letters.
"""


def read_input(fd):
    dots = set()
    folds = []
    for line in fd:
        stripped = line.strip()
        if stripped == '':
            break
        dots.add(tuple([int(x) for x in stripped.split(',')]))
    for line in fd:
        stripped = line.strip()
        split = stripped.split('=')
        folds.append((split[0], int(split[1])))
    return dots, folds


def print_dots(dots):
    max_y = range(max([y for _, y in dots]) + 1)
    max_x = max([x for x, _ in dots]) + 1
    for y in max_y:
        line = ''
        for x in range(max_x):
            line += '#' if (x, y) in dots else '.'
        print(line)


def fold(dots, fold_direction, fold_line):
    if fold_direction == 'fold along y':
        index = 1
    else:
        index = 0
    for dot in set(dots):
        if dot[index] > fold_line:
            dots.remove(dot)
            new_dot = list(dot)
            new_dot[index] = 2 * fold_line - dot[index]
            dots.add(tuple(new_dot))


def main():
    with open('input.txt') as fd:
        dots, folds = read_input(fd)
        for fold_direction, fold_line in folds:
            fold(dots, fold_direction, fold_line)
        print_dots(dots)


if __name__ == '__main__':
    main()
