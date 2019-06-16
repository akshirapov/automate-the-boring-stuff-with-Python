#! python3
# command_line_emailer.py - Sends email from command line.


import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

# Get mail and text
if len(sys.argv) >= 3:
    send_to = sys.argv[1]
    text = sys.argv[2]

# Open browser with link
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get('https://mail.ru/')

# Sign in
el_login = driver.find_element_by_id('mailbox:login')
el_password = driver.find_element_by_id('mailbox:password')

el_login.send_keys('command_line_mailer')
el_password.send_keys('YDfqRmDeFVRn')
el_password.submit()

# Open new mail
el_write_mail = WebDriverWait(driver, 10). \
    until(expected_conditions.element_to_be_clickable((By.XPATH, "//span[text()='Написать письмо']")))
el_write_mail.click()

# Fill contact and subject
el_inputs = WebDriverWait(driver, 10). \
    until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR,
                                                                "input.container--H9L5q.size_s_compressed--2c-eV")))
el_contact_to = el_inputs[0]
el_contact_to.send_keys(send_to)

el_subject = el_inputs[1]
el_subject.send_keys(text)

# Send
el_send = WebDriverWait(driver, 10). \
    until(expected_conditions.element_to_be_clickable((By.XPATH, "//span[text()='Отправить']")))
el_send.click()

# Confirm
el_spans = WebDriverWait(driver, 10). \
    until(expected_conditions.presence_of_all_elements_located((By.XPATH, "//span[text()='Отправить']")))
el_spans[1].click()
