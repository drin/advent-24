#!/usr/bin/env python

# ------------------------------
# License

# Copyright 2023 Aldrin Montana
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.


# ------------------------------
# Module Docstring
"""
Solution for Advent of Code Day 1.
"""


# ------------------------------
# Dependencies

import sys
from pathlib import Path


# ------------------------------
# Functions

def ValueFromMessage(encoded_msg, direction=1):
    """
    Scan :encoded_msg: in a :direction: (-1 or 1) for a numeric character.
    """

    for encoded_sym in encoded_msg[::direction]:
        try   : encoded_val = int(encoded_sym)
        except: encoded_val = -1

        if encoded_val >= 0: break

    return encoded_val


def ValueFromInput(in_stream):
    """ Scan every line in :in_stream: and sum the decoded values. """

    # sum each decoded value; each of which is:
    return sum([
        (
              # the first integer from the left  (10's place)
              10 * ValueFromMessage(encoded_msg, direction=1 )

              # the first integer from the right ( 1's place)
            +      ValueFromMessage(encoded_msg, direction=-1)
        )

        # scan :in_stream:
        for encoded_msg in in_stream
    ])


# ------------------------------
# Main

if __name__ == '__main__':
    # Input 1 can be found at `../inputs/day1.txt`
    input_fpath = Path(sys.argv[1])

    with input_fpath.open() as input_handle:
        calibration_value = ValueFromInput(input_handle)
        print(calibration_value)

