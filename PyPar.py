################################################################################
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <https://www.gnu.org/licenses/>.
#
################################################################################

APPLICATION_NAME = "PyPar"
APPLICATION_VERSION = "1.0.0.0"

import sys
import random
import argparse

def find_token(s, start, maxlen):
    i = start
    # skip whitespace
    while (i < len(s)) and (s[i].isspace()):
        i += 1
    # find token
    length = 0
    index = i
    while (i < len(s)) and (not s[i].isspace()) and (length < maxlen):
        length += 1
        i += 1
    return index, length
    
def format(s, indent, maxlen):
    width = maxlen - indent
    lines = []
    line = []
    line_length = 0
    index, length = find_token(s, 0, width)
    while length > 0:
        word = s[index:index + length]
        if line_length + len(word) <= width:
            line.append(word)
            line_length += len(word) + 1    # space
            if len(word) == width:  # line is full with one word
                lines.append(line)
                line = []
                line_length = 0
                width = maxlen
        else:
            lines.append(line)
            line = []
            width = maxlen
            line.append(word)
            line_length = len(word) + 1
        index, length = find_token(s, index + length, width)
    if len(line) > 0:
        lines.append(line)
    return lines

def line_width(line):
    if len(line) == 0:
        return 0
    l = 0
    for word in line:
        l += len(word) + 1  # space
    return l - 1    # no space after last word

def printx(lines, margin, indent, maxlen, justify):
    line_indent = indent    # indent first line
    lineno = 0
    while lineno < len(lines):
        line = lines[lineno]
        # ------- distribute remaining spaces -------
        if justify:
            if len(line) > 1:   # avoid problems with randint()
                remaining_spaces = maxlen - line_width(line) - line_indent
                n = len(line) - 1
                k = random.randint(0, n - 1)
                spaces = [0] * n
                while remaining_spaces > 0:
                    spaces[k] += 1
                    k += 1
                    if k == n:
                        k = 0
                    remaining_spaces -= 1
        # ------- print words -------
        print(' ' * (margin + line_indent), end='')
        nspaces = 0
        i = 0
        while i < len(line):
            print(line[i], end='')
            if justify:
                if lineno < len(lines) - 1:
                    if i < len(line) - 1:
                        nspaces = spaces[i] + 1
                    else:
                        nspaces = 0     # no spaces after last word in line
                else:
                    nspaces = 1
            else:
                nspaces = 1 if i < len(line) - 1 else 0
            print(' ' * nspaces, end='')
            i += 1
        print()
        line_indent = 0
        lineno += 1

def init():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--indent", type=int, default=10, help="first line paragraph indentation")
    ap.add_argument("-j", "--justify", action="store_true", help="justify text")
    ap.add_argument("-m", "--margin", type=int, default=0, help="left margin of text")
    ap.add_argument("-w", "--width", type=int, default=75, help="text width")
    ap.add_argument("FILE", type=argparse.FileType('r', encoding="utf-8"), nargs='*', help="input files")
    args = ap.parse_args()
    if args.width < 1:
        ap.error("-w/--width must be greater than 0")
    if args.indent >= args.width:
        ap.error("-i/--indent must be less than text width")
    if args.margin < 0:
        ap.error("-m/--margin must be greater than or equal to 0")
    if len(args.FILE) == 0:
        print(f"{ap.prog}: no input files")
    return args
    
def main():
    args = init()
    for f in args.FILE:
        for line in f:
            if line == '\n':
                print()
            else:
                lines = format(line, args.indent, args.width)
                printx(lines, args.margin, args.indent, args.width, args.justify)
        f.close()

if __name__ == "__main__":
    main()

