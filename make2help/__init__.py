import pathlib
import sys

from .make2help import format_makehelp


def main():
    """Search Makefile at current directory and show help."""
    makefile = pathlib.Path('./Makefile')
    if not makefile.is_file():
        print(
            'There is no Makefile at {}'.format(pathlib.Path('.').absolute()))
        sys.exit(1)
    for line in format_makehelp(makefile):
        print(line)
