# contact_form_automation
- Automated UI tests for the Notch contact form
- Website: [https://wearenotch.com/contact/](https://wearenotch.com/contact/)
- 📘 For more on the design strategy and test methodology, see [TEST_DESIGN.md](./TEST_DESIGN.md)
- 📋 For suggested enhancements and identified UX issues see [UI_IMPROVEMENTS.md](./UI_IMPROVEMENTS.md) 

---

# Setup and Prerequisites

- Download and install Google Chrome, as the tests are currently written for it. ChromeDriver is included in this repository.
- Clone this repository  
- Install Python 3.8+ and pip  
- Install project dependencies:

```bash
pip install -r requirements.txt
```

# Scripts

## `test_contact_form_positive.py`
- Tests obligatory fields in the contact form with valid inputs.
- A new unique email address is generated automatically for every run to avoid duplication errors.

## `test_contact_form_negative.py`
- Tests invalid contact form scenarios:
  - Missing First Name  
  - Missing Last Name  
  - Missing Email  
  - Invalid Email Format  
  - Unchecked Privacy Checkbox

## `test_fail_scenario.py`
- Tests fail scenario:
  - Missing First Name  
  - Asserts thank-you URL which we know it will fail

---

# Guidelines
## position yourself properly in the root folder (I used CMD for this task)
- cd Desktop\contact_form_automation  (this is my example)

## run wanted file from the root folder
- pytest tests/test_contact_form_negative.py -v
- pytest tests/test_contact_form_positive.py -v
- pytest tests/test_fail_scenario.py -v

## or run full suite
- pytest tests/ -v

## run from root and create reports
- pytest tests/test_contact_form_negative.py -v --html=reports/report.html
- pytest tests/test_contact_form_positive.py -v --html=reports/report.html
- pytest tests/test_fail_scenario.py -v --html=reports/report.html
- pytest tests/ -v --html=reports/report.html

## Additional notes:
- in conftest.py file choose headless option if wanted
- in utils/config.py change URL if needed
- in utils/helpers.py change email function to generate either new domain or local part


