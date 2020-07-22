# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pytest  # type: ignore

import nano_id.nano_id as do


def test_create_ok_size_and_alphabet_default():
    assert do.create(0, '') == '0123456789abcdef'


def test_create_ok_size_wun_and_alphabet_default(capsys):
    assert do.create(1, '') == '0'


def test_create_ok_size_wun_matches_alphabet_length(capsys):
    assert do.create(1, 'a') == 'a'


def test_create_ok_size_two_matches_twice_alphabet_length(capsys):
    assert do.create(2, 'a') == 'aa'
