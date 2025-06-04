# contains locators for the elements on the /contact page
# contains methods to interact with those elements

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class ContactPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.ID, "input_2_5")
        self.last_name_input = (By.ID, "input_2_18")
        self.email_input = (By.ID, "input_2_17")
        self.privacy_checkbox = (By.ID, "input_2_16_1")
        self.submit_button = (By.ID, "gform_submit_button_2")
        
        # Locating Accept All and Reject All buttons for the cookies pop-up
        self.cookie_accept_button = (By.CSS_SELECTOR, "button[data-cky-tag='accept-button']")
        self.cookie_reject_button = (By.CSS_SELECTOR, "button[data-cky-tag='reject-button']")

    def accept_cookie_consent(self, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(self.cookie_accept_button) # can also be replaced with reject_button
            ).click()
        except TimeoutException:
            # Pop-up not present, continue silently
            pass

    # finds three obligatory fields, sending the data
    def fill_required_fields(self, first_name, last_name, email):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.email_input).send_keys(email)

    # locates the checkbox (stored in the self.privacy_checkbox) and ticks if not selected
    def accept_privacy_policy(self):
        checkbox = self.driver.find_element(*self.privacy_checkbox)
        if not checkbox.is_selected():
            checkbox.click()

    # clicks the "Send message" button
    def submit_form(self):
        self.driver.find_element(*self.submit_button).click()
