#! python3

# Command Line Emailer - Automates emailing
# Usage - From the command line, enter 'cmdEmailer your_email password recipient_email message'
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys

# Log into email address and send message
if len(sys.argv) > 2:
    browser = webdriver.Firefox()
    browser.get('http://gmail.com')
    user = browser.find_element_by_css_selector('input[type="email"]')
    user.send_keys(sys.argv[1])
    nextButton = browser.find_element_by_class_name('CwaK9')
    nextButton.click()
    wait = WebDriverWait(browser, 10)
    password = browser.find_element_by_css_selector("input[type='password']")  # this is where the program crashes
    # password.send_keys(sys.argv[2])
    print(password)
    password.send_keys(sys.argv[2])
    nextButton.click()
    compose = browser.find_element_by_css_selector('.z0')
    compose.click()
    recipient = browser.find_element_by_id(':af')
    recipient.send_keys(sys.argv[3])
    recipient.send_keys(Keys.RETURN)
    subject = browser.find_element_by_id(':9y')
    subject.send_keys('From: Jeff Moorhead - Email sent with Python.')
    subject.send_keys(Keys.RETURN)
    message = ' '.join(sys.argv[4:])
    compose = browser.find_element_by_id(':az')
    compose.send_keys(message + '\n\nThank you,\nJeff Moorhead')
    send = browser.find_element_by_id(':9o')
    send.click()

    print('Message sent:\n\n' + message)
else:
    print('Emailer usage: enter command line arguments as follows...\n\ncmdEmailer YOUR_EMAIL PASSWORD RECIPIENT_EMAIL'
          'message')
