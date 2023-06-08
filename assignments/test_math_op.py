import pytest
import logging


def divide(a, b):
    result = a / b

    if result > 10:
        logging.info("Result is greater than 10")
    else:
        logging.info("Result is less than or equal to 10")
    return result


def test_divide(caplog):
    # Set the log level to capture only warnings and above
    caplog.at_level(logging.WARNING)

    # Perform the test
    result = divide(20, 2)

    assert result == 10.0

    # Check log messages
    assert "Result is less than or equal to 10" not in caplog.text
    assert "Result is greater than 10" in caplog.text

