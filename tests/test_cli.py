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
