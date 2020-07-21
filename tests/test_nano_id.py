# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pytest  # type: ignore

import nano_id.nano_id as do


def test_create_ok_size_and_alphabet_default():
    assert do.create(0, '') == '0123456789abcdef'
