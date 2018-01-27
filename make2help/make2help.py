"""
make2help

See: https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
"""

import re


def _parse_makefile(lines):
    lines = [line for line in lines if line != '']
    pattern = re.compile('(?<=^## ).+')
    head_pattern = re.compile('.+(?=:)')
    for first, second in zip(lines, lines[1:]):
        if first.startswith('##'):
            detail = pattern.search(first.strip()).group().strip()
            target = head_pattern.search(second.strip()).group()
            yield target, detail


def _prepare_makefile_lines(makefile_path):
    with open(makefile_path, 'r') as makefile:
        lines = makefile.readlines()
    return lines


def format_makehelp(makefile_path):
    """
    return Makefile help.
    """
    lines = _prepare_makefile_lines(makefile_path)
    helps = _parse_makefile(lines)
    return ('{}:\t{}'.format(target, detail) for target, detail in helps)
