# Data-Driven Password Validation Tester (Selenium & Python)

This is a QA automation project built to demonstrate data-driven testing principles. The script validates a password form by executing a user-defined number of automated tests against a live, hosted web page.

**Live Test Site:** [https://viktor537.github.io/selenium-password-tester/](https://viktor537.github.io/selenium-password-tester/)

---

## Project Overview

The script is structured around a central function, `password_testing_script()`, which accepts the total number of tests to be executed as an argument.

The script performs the following actions:

* Generates a unique random password (with a length between 1 and 25 characters) for each test iteration.
* Loops through the specified number of tests (e.g., 100 times, as defined in the function call).
* Submits each unique password to the form and waits for the site to respond.
* Validates the site's reaction by checking the resulting CSS class (`.success` or `.error`) of the result message.
* Compares the site's actual reaction against the *expected* business logic (e.g., a 4-character password *must* produce an error).
* Collects all failed test cases (where the site's logic failed) and prints a final summary to the console.

---

## Technology Stack

* **Python**
* **Selenium WebDriver**
* **GitHub Pages** (Used to host the static test environment)
* **HTML/CSS/JS** (Used to build the test site itself)

---


## How to Run

1.  **Clone the repository:**
    ```bash
    git clone [https://viktor537.github.io/selenium-password-tester.git](https://viktor537.github.io/selenium-password-tester.git)
    ```
2.  **Install dependencies:**
    ```bash
    pip install selenium
    ```
3.  **Ensure WebDriver is available:**
    Make sure `chromedriver` (or your browser's driver) is in your system's PATH.
4.  **Run the script:**
    ```bash
    python main.py
    ```
    *Note: The number of tests to run can be modified by changing the argument in the `password_testing_script(100)` call at the end of the script.*
