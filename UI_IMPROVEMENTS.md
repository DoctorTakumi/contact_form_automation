# ✨ Usability & UX Improvement Suggestions – Notch Contact Page

This document outlines user experience (UX) and functionality improvements for the [Notch Contact Page](https://wearenotch.com/contact/) based on manual testing and test automation analysis.

---

## ✅ Current Identified Issues

### 1. Lack of Feedback When Privacy Policy Checkbox Is Unchecked

- **Problem:** If the user fills in all mandatory fields but does **not check the Privacy Policy checkbox**, the page simply reloads with no visible error or feedback.
- **Impact:** If the user is unaware that successful submissions redirect to the "Thank You" page, they may be confused when nothing happens. The validation message *"This field is required."* is present but only becomes visible after manually scrolling down to the checkbox.
- **Suggested Improvement:** Automatically scroll to the checkbox field when validation fails, ensuring the user can immediately see the *"This field is required."* message without needing to manually scroll.

---

### 2. Lack of Input Validation for Name Fields

**Problem:** The form accepts invalid characters in the "First Name" and "Last Name" fields. For example, inputs like `!"#$` for first name and `-30` for last name are considered valid, and the form is successfully submitted.

**Impact:** This can lead to poor data quality, potential spam, and credibility issues, especially if contact form submissions are stored or forwarded to a CRM or email system.

**Suggested Improvement:** Implement stricter frontend and backend validation for name fields. Allow only alphabetic characters and common name symbols (e.g., hyphens or apostrophes) while rejecting clearly invalid inputs such as numbers or special characters. Display user-friendly error messages when invalid input is detected.

---

### 3. "What services do you need?" Appears Required But Allows Submission Without Selection

- **Problem:** The option labeled `"What services do you need*"` includes an asterisk, implying it's required — yet the form can be submitted without making a selection.
- **Impact:** Creates user confusion and violates form design best practices.
- **Suggested Improvement:** Either:
  - Remove the asterisk if the field is optional  
  **OR**
  - Enforce it as required and show a message like:  
    > "Please select at least one service."

---

### 4. Rate Limiting Without Explanation

- **Problem:** After submitting the form multiple times (even with valid new email addresses), a generic error appears under the email field:  
  > "Form cannot be submitted"
- **Impact:** No context is given for the rejection (rate limit, spam protection, etc.), which may confuse users.
- **Suggested Improvement:** Show a clearer error message like:  
  > "You've reached the maximum number of submissions. Please try again later or contact us directly."

---

### 5. Ambiguous Error Message Despite 204 No Content Response

**Problem:**  
When submitting the form with valid data and ticking the Privacy Policy checkbox, a message saying **"Form cannot be submitted."** is shown on the frontend. However, in the browser DevTools, the server returns a **204 No Content** response, which typically indicates a successful request.

**Impact:**  
This creates confusion for both users and developers:
- **Users** see a generic error message without explanation or any context on why the form cannot be submitted, despite providing valid inputs.
- **Developers or testers** may be misled by the 204 status code, which conventionally signals a successful action with no response body.
- **Suggested Improvement:**  
- Ensure that **server-side validation** returns an appropriate error status code (e.g., `400` or `422`) when the submission fails.
- Display a **more descriptive error message** on the frontend to inform users why the form could not be submitted (e.g., rate limit exceeded, suspected spam, server error, etc.).

---

## 🛠 Additional Suggestions

### 1. Scroll-to-Validation Feedback

- **Problem:** If errors occur outside of the current scroll view (like the checkbox), the user won’t know.
- **Suggested Improvement:** Auto-scroll to the first validation error or display a banner at the top indicating an issue.


---

## ⚠️ Risks to Automation Stability

These issues may affect test reliability:

- ❗ **Unpredictable error handling:** Lack of consistent, visible error messages can cause automated test scripts to fail silently.
- ❗ **Rate limits on submissions** may cause tests to fail if run repeatedly.
- ❗ **Dynamic behavior (scroll-dependent validation)** complicates assertion logic unless automated scrolling or error detection is implemented.

---