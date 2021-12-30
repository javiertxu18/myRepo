import logging

from src.main.scripts.functions.generalFunctions import encript, setLogger, getLogger
import pytest


@pytest.fixture()
def name(pytestconfig):
    return pytestconfig.getoption("name")


@pytest.mark.parametrize("t_in, t_out", [("GeeksforGeeks", "f1e069787ece74531d112559945c6871")])
def test_encript(t_in, t_out):
    assert encript(t_in) == t_out


def test_setLogger_1():
    assert setLogger() == True


@pytest.mark.parametrize("t_in, t_out", [
    ("peter", getLogger("peter")),
    ("juan", getLogger("juan")),
    ("iker", getLogger("iker"))
])
def test_setLogger_2(t_in, t_out):
    assert setLogger(t_in) == t_out


@pytest.mark.parametrize("t_in, t_out", [
    ("peter", logging.getLogger("peter")),
    ("juan", logging.getLogger("juan")),
    ("iker", logging.getLogger("iker"))
])
def test_getLogger(t_in, t_out):
    assert getLogger(t_in) == t_out
