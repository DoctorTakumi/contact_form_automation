import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.config import BASE_URL

@pytest.fixture
def driver():
    options = Options()

    # Toggle headless mode by commenting/uncommenting the next two lines
    # options.add_argument("--headless")
    # options.add_argument("--window-size=1920,1080")
    # options.add_argument("--disable-gpu")  # Optional – only add if you hit rendering issues

    driver = webdriver.Chrome(options=options)
    driver.get(BASE_URL)
    driver.maximize_window()  # Comment out for headless if needed

    yield driver

    driver.quit()
