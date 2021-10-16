from madlib_cli import __version__
import pytest
from madlib_cli.madlib import read_file


def test_read_file_returns_stripped_string():
    """
    test a file if we can read the contents of it
    """
    actual = read_file("assets/example.txt")
    expected = "It was a {Adjective} and {Adjective} {Noun}."
    assert actual == expected



def test_version():
    assert __version__ == '0.1.0'        