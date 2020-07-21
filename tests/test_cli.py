# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pytest  # type: ignore

import nano_id.cli as cli


def test_main_ok_size_and_alphabet_default():
    assert cli.main([0, '']) is None
    out, err = capsys.readouterr()
    assert out == '0123456789abcdef'
