"""
--- Part Two ---
Through a little deduction, you should now be able to determine the remaining
digits. Consider again the first example above:

acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
cdfeb fcadb cdfeb cdbaf
After some careful analysis, the mapping between signal wires and segments only
make sense in the following configuration:

 dddd
e    a
e    a
 ffff
g    b
g    b
 cccc
So, the unique signal patterns would correspond to the following digits:

acedgfb: 8
cdfbe: 5
gcdfa: 2
fbcad: 3
dab: 7
cefabd: 9
cdfgeb: 6
eafb: 4
cagedb: 0
ab: 1
Then, the four digits of the output value can be decoded:

cdfeb: 5
fcadb: 3
cdfeb: 5
cdbaf: 3
Therefore, the output value for this entry is 5353.

Following this same process for each entry in the second, larger example above,
the output value of each entry can be determined:

fdgacbe cefdb cefbgd gcbe: 8394
fcgedb cgb dgebacf gc: 9781
cg cg fdcagb cbg: 1197
efabcd cedba gadfec cb: 9361
gecf egdcabf bgf bfgea: 4873
gebdcfa ecba ca fadegcb: 8418
cefg dcbef fcge gbcadfe: 4548
ed bcgafe cdgba cbgef: 1625
gbdfcae bgc cg cgb: 8717
fgae cfgab fg bagce: 4315
Adding all of the output values in this larger example produces 61229.

For each entry, determine all of the wire/segment connections and decode the
four-digit output values. What do you get if you add up all of the output
values?
"""


class Parser:
    def __init__(self):
        self.digits = {}
        self.unknown = []

    def learn(self, value):
        if len(value) == 2:
            self.set_digit(1, value)
        elif len(value) == 3:
            self.set_digit(7, value)
        elif len(value) == 4:
            self.set_digit(4, value)
        elif len(value) == 7:
            self.set_digit(8, value)
        else:
            self.unknown.append(value)

    def set_digit(self, digit, value):
        self.digits[digit] = value

    def guest(self):
        while self.unknown:
            value = self.unknown.pop()
            if len(value) == 5:
                if self.number_of_segments_without(value, 1) == 3:
                    self.set_digit(3, value)
                elif self.number_of_segments_without(value, 4) == 3:
                    self.set_digit(2, value)
                else:
                    self.set_digit(5, value)
            else:
                if self.number_of_segments_without(value, 7) == 4:
                    self.set_digit(6, value)
                elif self.number_of_segments_without(value, 4) == 3:
                    self.set_digit(0, value)
                else:
                    self.set_digit(9, value)

    def number_of_segments_without(self, value, digit):
        return len(value - self.digits[digit])

    def get_digit_by_value(self, value):
        for digit, code in self.digits.items():
            if code == value:
                return digit

    def to_integer(self, message):
        result = 0
        for index, values in enumerate(reversed(message)):
            result += pow(10, index) * self.get_digit_by_value(values)
        return result


def read_input(line):
    return [[set(value) for value in group.split(' ')] for group in line.strip().split(' | ')]


def main():
    with open('input.txt') as fd:
        result = 0
        for line in fd:
            digits, message = read_input(line)
            parser = Parser()
            for values in digits:
                parser.learn(values)
            parser.guest()
            result += parser.to_integer(message)
        print(result)


if __name__ == '__main__':
    main()
