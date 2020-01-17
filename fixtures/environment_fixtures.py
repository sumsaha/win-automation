import pytest
from wrappers.win_driver import WinDriver


@pytest.fixture()
def get_environment():
    driver = WinDriver()
    return driver

