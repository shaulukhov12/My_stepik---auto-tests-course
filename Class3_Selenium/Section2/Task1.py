from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector('#input_value') #.form-group .nowrap[id]
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_css_selector('.form-control')
    input1.send_keys(y)

    checkbox = browser.find_element_by_css_selector('[id="robotCheckbox"]')
    checkbox.click()

    button1 = browser.find_element_by_css_selector('[id="robotsRule"]')
    button1.click()

    submit = browser.find_element_by_css_selector('.btn.btn-default')
    submit.click()


finally:
    time.sleep(15)
    browser.quit()