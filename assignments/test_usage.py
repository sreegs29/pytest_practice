import pytest


@pytest.mark.resource
def test_resource_usage(virtual_memory_usage, cpu_usage):
    assert virtual_memory_usage < 20
    assert cpu_usage < 20

