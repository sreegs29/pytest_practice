import pytest
import random


@pytest.fixture
def generate_num():
    num_list = []
    for _ in range(0, 5):
        num_list.append(random.randint(1, 101))
    return num_list


def test_div_list_5(generate_num):
    for i in generate_num:
        assert i % 5 == 0

