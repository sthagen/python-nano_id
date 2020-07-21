#! /usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=line-too-long
"""Yet another nano id implementation."""
import sys

from nano_id.nano_id import create


# pylint: disable=expression-not-assigned
def main(argv=None):
    """Test driver for yet another implementation of nano id reading fromstdin and writing to stdout."""
    size = (sys.argv[1] if argv is None else argv[0]
    alphabet = sys.argv[2] if argv is None else argv[1]
    sys.stdout.write(create(size, alphabet))
    
