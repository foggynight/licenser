#!/usr/bin/env python3

# --- licenser ---
#
# Import a license into source code.
#
# Copyright (C) 2020 Robert Coffey
# Licensed under the GNU GPLv2

from pathlib import Path
from sys import argv

def process_args():
    """
    Process the command line arguments, getting the license filepath,
    preamble filepath, and a list of file extensions.

    Should either argument be omitted, it will be gotten from an input
    prompt in the program.

    @returns:
    - license {str|None}: Path to the license file
    - preamble {str|None}: Path to the preamble file
    - exts {[str]|None}: A list of file extensions
    """
    license = preamble = exts = None
    argc = len(argv)
    if argc > 3:
        exts = []
        for i in range(argc-3):
            exts.append(argv[i+3])
    if argc > 2:
        preamble = open(argv[2]).readlines()
    if argc > 1:
        license = open(argv[1]).readlines()
    return license, preamble, exts

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
            file = open(input(msg))
        except:
            print('Error: Cannot open file, try again')
    return file.readlines()

if __name__ == '__main__':
    license, preamble, exts = process_args()

    if not license: license = get_text('License path: ')
    if not preamble: preamble = get_text('Preamble path: ')
    if not exts: exts = input('File extensions: ').split()

    targs = []
    for ext in exts:
        targs.extend([str(e) for e in Path('.').glob(f'**/*.{ext}')])

    open('LICENSE', 'w').writelines(license)

    for file in targs:
        old = open(file).readlines()
        open(file, 'w').writelines(preamble + old)
