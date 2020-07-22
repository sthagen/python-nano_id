#! /usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=line-too-long
"""Yet another nano id implementation."""
import random

ENCODING = "utf-8"
ENCODING_ERRORS_POLICY = "ignore"


def create(size: int = None, alphabet: str = None):
    """Create a nano id of given size using the given alphabet or defaults."""
    if not alphabet:
        alphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-.:,;'
    if not size:
        size = 16
    return ''.join(random.SystemRandom().choice(alphabet) for _ in range(size))
