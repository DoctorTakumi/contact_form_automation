import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.contact_page import ContactPage
from utils.config import BASE_URL
from utils.helpers import get_next_email

# Fail Scenario: Missing First Name
def test_missing_first_name(driver):
    contact_page = ContactPage(driver)
    contact_page.accept_cookie_consent()
    contact_page.fill_required_fields(
        first_name="",  # missing first name
        last_name="Prezime",
        email=get_next_email()
    )
    contact_page.accept_privacy_policy()
    contact_page.submit_form()

    # Wait for the redirect to happen (explicit wait)
    WebDriverWait(driver, 5).until(EC.url_to_be("https://wearenotch.com/thank-you/"))

    # Expecting thank-you page — but it won’t redirect → this will FAIL
    assert driver.current_url == "https://wearenotch.com/thank-you/"
    
    
# ---------------------------- NOTES --------------------------
# This is simple test script written to demonstrate a failing scenario