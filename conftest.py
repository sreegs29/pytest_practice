import pytest
import psutil


@pytest.fixture
def input_value():
    input = 39
    return input


@pytest.fixture
def virtual_memory_usage():
    ram_usage = psutil.virtual_memory().percent
    return ram_usage


@pytest.fixture
def cpu_usage():
    cpu = psutil.cpu_percent()
    return cpu
