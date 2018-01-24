"""
make2help

See: https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
"""

import pathlib
import re
import sys


def _parse_makefile(lines):
    lines = [line for line in lines if line != '']
    helps = []
    pattern = re.compile('(?<=^## ).+')
    for idx, line in enumerate(lines):
        if line.startswith('##'):
            detail = pattern.search(line.strip()).group().strip()
            target = lines[idx + 1].strip()[:-1]
            helps.append((target, detail))
    return helps


def _prepare_makefile_lines(makefile_path):
    with open(makefile_path, 'r') as makefile:
        lines = makefile.readlines()
    return lines


def format_makehelp(makefile_path):
    lines = _prepare_makefile_lines(makefile_path)
    helps = _parse_makefile(lines)
    return ['{}:\t{}'.format(target, detail) for target, detail in helps]


def main():
    makefile = pathlib.Path('./Makefile')
    if not makefile.is_file():
        print(
            'There is no Makefile at {}'.format(pathlib.Path('.').absolute()))
        sys.exit(1)
    for line in format_makehelp(makefile):
        print(line)


if __name__ == '__main__':
    main()
