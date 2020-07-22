# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pytest  # type: ignore

import nano_id.nano_id as do

DEFAULT_SIZE_HACK = 16
DEFAULT_ALPHABET_HACK = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-.:,;'


def test_create_ok_size_and_alphabet_default():
    identity = do.create(0, '')
    assert len(identity) == DEFAULT_SIZE_HACK
    assert all(ch in DEFAULT_ALPHABET_HACK for ch in identity)


def test_create_ok_size_wun_and_alphabet_default(capsys):
    identity = do.create(1, '')
    assert len(identity) == 1
    assert all(ch in DEFAULT_ALPHABET_HACK for ch in identity)


def test_create_ok_size_wun_matches_alphabet_length(capsys):
    assert do.create(1, 'a') == 'a'


def test_create_ok_size_two_matches_twice_alphabet_length(capsys):
    assert do.create(2, 'a') == 'aa'


def test_create_ok_size_five_matches_twice_alphabet_length_plus_wun(capsys):
    assert do.create(5, 'ab') == 'ababa'
