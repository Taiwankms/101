import pytest
import time
from selenium import webdriver


@pytest.fixture
def stock():
    url = "https://piter-online.net/"
    pytest.driver = webdriver.Chrome()
    pytest.driver.get(url)
    time.sleep(2)

    yield

    pytest.driver.quit()

