import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.contact_page import ContactPage
from utils.config import BASE_URL
from utils.helpers import get_next_email


# Negative: Missing First Name
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

    # Assert: should still be on the contact page
    assert driver.current_url == BASE_URL
    
# Negative: Missing Last Name
def test_missing_last_name(driver):
    contact_page = ContactPage(driver)
    contact_page.accept_cookie_consent()
    contact_page.fill_required_fields(
        first_name="Ime",
        last_name="",  # missing last name
        email=get_next_email()
    )
    contact_page.accept_privacy_policy()
    contact_page.submit_form()

    assert driver.current_url == BASE_URL

# Negative: Missing Email
def test_missing_email(driver):
    contact_page = ContactPage(driver)
    contact_page.accept_cookie_consent()
    contact_page.fill_required_fields(
        first_name="Ime",
        last_name="Prezime",
        email=""  # missing email
    )
    contact_page.accept_privacy_policy()
    contact_page.submit_form()

    assert driver.current_url == BASE_URL

# Negative: Invalid Email Format
def test_invalid_email_format(driver):
    contact_page = ContactPage(driver)
    contact_page.accept_cookie_consent()
    contact_page.fill_required_fields(
        first_name="Ime",
        last_name="Prezime",
        email="abc"  # invalid format
    )
    contact_page.accept_privacy_policy()
    contact_page.submit_form()

    assert driver.current_url == BASE_URL

# Negative: Unchecked Privacy Checkbox
def test_unchecked_privacy_checkbox(driver):
    contact_page = ContactPage(driver)
    contact_page.accept_cookie_consent()
    contact_page.fill_required_fields(
        first_name="Ime",
        last_name="Prezime",
        email=get_next_email()
    )
    # do NOT accept privacy policy
    contact_page.submit_form()

    assert driver.current_url == BASE_URL
    
    
# ---------------------------- NOTES --------------------------
# This is simple test suite to verify negative scenario - missing (or invalid) entry data and website unable to submit the form due to that
# I added only asserts to verify that URL is going to stay the same - no redirect since we can't submit the form due to missing or invalid inputs
# generally, the next step would be to add asserts for the red fields showing that entry data is missing or it's invalid form
# furthermore, asserts to match warning message that entry data is missing or it's invalid form
# e.g. "The email address entered is invalid, please check the formatting (e.g. email@domain.com)."

