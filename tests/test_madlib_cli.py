from madlib_cli import __version__
from madlib_cli.madlib_cli import  read_template,parse_template,merge

def test_version():
    assert __version__ == '0.1.0'


def test_read_template_test():
    assert read_template("") == "sorry I can't open the game file"
    with open("madlib_cli/assest/small_example.txt") as file:
        assert read_template("madlib_cli/assest/small_example.txt") == file.read()


def test_parse_template():
    assert parse_template("hi {hi} hi") == (["{hi}"],"hi {} hi")

def test_merge():
    assert merge(["hi"],"hi {} hi") == "hi hi hi"
