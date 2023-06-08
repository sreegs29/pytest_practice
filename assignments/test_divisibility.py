import pytest
import logging


@pytest.mark.parametrize("num", [[(15, 20, 80), (10, 20, 72)]])
def test_divisible_by_5(num, caplog=None):
    caplog.set_level(logging.WARNING)
    for ele in num:
        for i in ele:
            assert i % 5 == 0


