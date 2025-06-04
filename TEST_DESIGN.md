# 🧪 Test Design and Implementation

## 🎯 Design Principles

- **Black-box testing approach**: I did not rely on internal code but tested the form purely based on expected UI behavior.
- **Modularization using POM (Page Object Model)**: All selectors and form interactions are abstracted into a `ContactPage` class for reusability and easy maintenance.
- **Separation of concerns**: Test files are grouped into:
  - **positive tests**: valid inputs that should allow form submission
  - **negative tests**: invalid or missing inputs that should prevent submission
  - **fail tests**: scenarios intentionally built to fail for demonstration purpose

## 🧠 Test Case Selection Strategy

- **Required field validation**: Ensured all required fields (`first name`, `last name`, `email`, `privacy checkbox`) are tested for absence.
- **Email format validation**: Included test with invalid email format (`abc`) to verify frontend regex or format validation.
- **Success case**: Valid inputs across all required fields and submission flow tested for redirect to thank-you page.
- **Failure demo**: Wrote a failing test to prove assertion and report logging behavior.
- **Dynamic data**: Unique emails are generated per test run to avoid “duplicate submission” logic.

## ⚙️ Implementation Approach

- **Selenium WebDriver** is used to control Chrome.
- **Pytest** is the test runner with fixtures to manage setup/teardown.
- **pytest-html** is used to generate human-readable reports.
- Test structure mimics real-world automation best practices with:
  - Shared fixtures in `conftest.py`
  - Utility methods in `helpers.py`
  - Base URL defined in `config.py`

## 📌 Future Improvements

- Add assertions for validation messages (e.g., red warning text below inputs etc.)
- Parametrize test cases for more coverage
- Extend POM for additional fields and edge cases

