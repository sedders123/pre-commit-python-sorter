from __future__ import print_function

import argparse
import os

from isort import isort


def imports_incorrect(filename):
    return isort.SortImports(filename, check=True).incorrectly_sorted


def main(argv=None):
    for filename in args.filenames:
        if imports_incorrect(filename):
            isort.SortImports(filename)
            print('FIXED: {0}'.format(os.path.abspath(filename)))
    return 0

if __name__ == '__main__':
    exit(main())
