#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-2.0

# --- licenser ---
#
# Import a license into source code.
#
# Copyright (C) 2020 Robert Coffey

from pathlib import Path

def get_text(msg):
    """
    Get the text content from a file located at the path obtained
    through a call to input.

    @params
    - msg {str}: Input prompt message

    @return {[str]}: Text content as a list of lines
    """
    file = None
    while not file:
        try:
            path = input(msg)
            file = open(path)
        except:
            print('Error: Cannot open file, try again')
    return file.readlines()

def main():
    # Get license and preamble
    license = get_text('License path: ')
    preamble = get_text('Preamble path: ')

    # Get list of target source files
    exts = input('File extensions: ').split()
    targs = []
    for ext in exts:
        targs.extend([str(e) for e in Path('.').glob(f'**/*.{ext}')])

    # Copy license to target dir
    open('LICENSE', 'w').writelines(license)

    # Copy file preamble to all source files
    for file in targs:
        old = open(file).readlines()
        open(file, 'w').writelines(preamble + old)

if __name__ == '__main__':
    main()
