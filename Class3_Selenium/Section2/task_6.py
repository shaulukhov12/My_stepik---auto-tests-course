from selenium import webdriver
import time
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'text.txt')

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector("[name='firstname']")
    input1.send_keys("Azret")

    input2 = browser.find_element_by_css_selector("[name='lastname']")
    input2.send_keys('Shaulukhov')

    input3 = browser.find_element_by_css_selector("[name='email']")
    input3.send_keys('shaulukhov12@gmail.com')

    input_file = browser.find_element_by_css_selector("[name='file']")
    input_file.send_keys(file_path)

    submit = browser.find_element_by_css_selector('.btn.btn-primary')
    submit.click()

finally:
    time.sleep(15)
    browser.quit()