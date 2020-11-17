#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-2.0

# --- licenser ---
#
# Import a license into source code.
#
# Copyright (C) 2020 Robert Coffey

def get_text(msg):
    """
    Get the text content from a file.

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
    # get desired license
    license = get_text('License path: ')

    # get desired file preamble
    preamble = get_text('Preamble path: ')

    # get list of target source files
    # copy license to target dir
    # copy file preamble to all source files

if __name__ == '__main__':
    main()
