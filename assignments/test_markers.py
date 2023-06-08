import pytest
import logging


@pytest.mark.even
def test_even(caplog):
    caplog.at_level()
    num = 20
    assert num % 2 == 0


