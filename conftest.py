from driver import Driver
import pytest

@pytest.fixture(scope='session', autouse=True)
def start():
    Driver.start()
