"""
--- Part Two ---
On the other hand, it might be wise to try a different strategy: let the giant
squid win.

You aren't sure how many bingo boards a giant squid could play at once, so
rather than waste time counting its arms, the safe thing to do is to figure out
which board will win last and choose that one. That way, no matter which boards
it picks, it will win for sure.

In the above example, the second board is the last to win, which happens after
13 is eventually called and its middle column is completely marked. If you were
to keep playing until this point, the second board would have a sum of unmarked
numbers equal to 148 for a final score of 148 * 13 = 1924.

Figure out which board will win last. Once it wins, what would its final score
be?
"""
import re


class Board:
    def __init__(self):
        self.rows = []

    def add_row(self, row):
        self.rows.append(re.split(r'\s+', row))

    def draw(self, number):
        for row in self.rows:
            if number in row:
                index = row.index(number)
                row[index] = ''

    def is_win(self):
        board_size = 5
        for row in range(board_size):
            if self.no_values_in_range([row], range(board_size)):
                return True
        for col in range(board_size):
            if self.no_values_in_range(range(board_size), [col]):
                return True
        return False

    def no_values_in_range(self, row_func, col_func):
        for row in row_func:
            for col in col_func:
                value = self.rows[row][col]
                if value != '':
                    return False
        return True

    def get_score(self, last_number):
        result = 0
        for row in self.rows:
            for col in row:
                if col != '':
                    result += int(col)
        return result * int(last_number)

    def __repr__(self):
        r = ''
        for row in self.rows:
            for col in row:
                if len(col) == 0:
                    r += '   '
                elif len(col) == 1:
                    r += '  ' + col
                else:
                    r += ' ' + col
                r += '|'
            r += '\n'
        return r


def main():
    with open('input.txt') as fd:
        numbers = fd.readline().strip()
        boards = fill_boards(fd)

        for number in numbers.split(','):
            for board in boards:
                board.draw(number)
            for board in boards:
                if board.is_win():
                    boards.remove(board)
                    if not boards:
                        print(board.get_score(number))
                        return


def fill_boards(fd):
    boards = []
    for line in fd:
        board_line = line.strip()
        if board_line == '':
            boards.append(Board())
        else:
            boards[-1].add_row(board_line)
    return boards


if __name__ == '__main__':
    main()
