import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.contact_page import ContactPage
from utils.config import BASE_URL
from utils.helpers import get_next_email


# accept cookie pop-up,, fill in the required fields, call function that generates new emails based on current UNIX timestamp in seconds
# clicking the privacy_policy tickbox and clicking "Send message" button
def test_fill_required_fields_and_submit(driver):
    contact_page = ContactPage(driver)
    contact_page.accept_cookie_consent()  # Accept cookie pop-up
    contact_page.fill_required_fields(
        first_name="ime",
        last_name="prezime",
        email=get_next_email()
    )
    contact_page.accept_privacy_policy()
    contact_page.submit_form()
    
    # Wait for the redirect to happen (explicit wait)
    WebDriverWait(driver, 10).until(EC.url_to_be("https://wearenotch.com/thank-you/"))

    # Assert the current URL to confirm the form was submitted successfully
    assert driver.current_url == "https://wearenotch.com/thank-you/"
    
    # time.sleep(3)  # wait to visually confirm if wanted, can be commented out  
    
    
# ---------------------------- NOTES --------------------------
# This is simple test suite to verify positive scenario - valid data entered in obligatory fields, submitted, webpage redirected
