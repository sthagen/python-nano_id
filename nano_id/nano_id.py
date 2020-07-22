#! /usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=line-too-long
"""Yet another nano id implementation."""

ENCODING = "utf-8"
ENCODING_ERRORS_POLICY = "ignore"


def create(size: int = None, alphabet: str = None):
    """Create a nano id of given size using the given alphabet or defaults."""
    if not alphabet:
        alphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-.:,;'
    if not size:
        size = 16
    nano = []
    while len(nano) < size:
        nano.extend([ch for ch in alphabet])
    return ''.join(nano[:size])
