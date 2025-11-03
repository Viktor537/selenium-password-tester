import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from time import sleep


def generate_password(length=None):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    characters = ['*', '&', '$', '#']
    all_characters_combined = letters + numbers + characters
    password = ""

    if length is None:
        password_length = random.choice(range(1, 16))
    else:
        password_length = int(length)

    for character in range(password_length):
        password += random.choice(all_characters_combined)

    return password


def find_inputs(w):
    password_field = w.until(ec.presence_of_element_located((By.ID, 'password-input')))
    submit_button = w.until(ec.presence_of_element_located((By.ID, 'submit-btn')))

    return password_field, submit_button


def test_one_password(browser, password_field, submit_button, password_to_test):
    password_field.clear()
    password_field.send_keys(password_to_test)
    submit_button.click()
    try:
        WebDriverWait(browser, 0.1).until(ec.visibility_of_element_located((By.CLASS_NAME, 'error')))
        print(f"Test case with: '{password_to_test}': Fail (Password length is: {len(password_to_test)} symbol/s. )")
        return True
    except TimeoutException:
        WebDriverWait(browser, 0.1).until(ec.visibility_of_element_located((By.CLASS_NAME, 'success')))
        print(f"Test case with: '{password_to_test}': Pass (Error message not found)")
        return False


def print_failed_passwords(failed_passwords, browser):
    sleep(2)
    browser.close()
    print(f"These are all the passwords that failed: {failed_passwords}")


def Password_testing_script(numbers_of_tests):
    for i in range(int(numbers_of_tests)):
        password_to_test = generate_password()
        result_from_test = test_one_password(browser, password_field, submit_button, password_to_test)
        if result_from_test:
            all_failed_passwords.append(password_to_test)
    print_failed_passwords(all_failed_passwords, browser)

browser = webdriver.Chrome()
browser.get('https://viktor537.github.io/selenium-password-tester/')
wait = WebDriverWait(browser, 5)

password_field, submit_button = find_inputs(wait)
all_failed_passwords = []
Password_testing_script(10)