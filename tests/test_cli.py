# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pytest  # type: ignore

import nano_id.cli as cli


def test_main_ok_size_and_alphabet_default(capsys):
    assert cli.main([0, '']) is None
    out, _ = capsys.readouterr()
    assert out == '0123456789abcdef'


def test_main_nok_size_wrong_type_default_alphabet():
    message = r"invalid literal for int\(\) with base 10: 'a'"
    with pytest.raises(ValueError, match=message):
        cli.main(['a', ''])


def test_main_nok_negative_size_default_alphabet():
    message = r"size must be either positive or zero \(for default\)"
    with pytest.raises(ValueError, match=message):
        cli.main([-1, ''])


def test_main_nok_size_wun_but_alphabet_has_wrong_type():
    message = r"'int' object is not subscriptable"
    with pytest.raises(TypeError, match=message):
        cli.main([1, 42])
