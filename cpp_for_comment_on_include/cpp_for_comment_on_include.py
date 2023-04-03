
import argparse
import os
from typing import Sequence

EXTENSIONS = tuple(['.h', '.hpp', '.cpp', '.cxx', '.cc'])
INCLUDE_STRING = "#include"
FOR_COMMENT = "// for "


def for_comment_on_include(file, filename: str = '<unknown>') -> int:
    """Returns a non-zero value if given file contains include statements that
    are not followed by a "// for " comment.
    """

    for (i, line) in enumerate(file, 1):
        if i == 1:
            continue
        if INCLUDE_STRING in line:
            if FOR_COMMENT not in line:
                print(f'{filename}:{i}: Missing "// for" comment for include.')
                return 1
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args(argv)

    retv = 0

    for filename in args.filenames:
        if os.path.isdir(filename):
            continue
        if not filename.endswith(EXTENSIONS):
            continue
        with open(filename, 'r') as f:
            retv |= for_comment_on_include(f, filename=filename)

    return retv


if __name__ == '__main__':
    raise SystemExit(main())
