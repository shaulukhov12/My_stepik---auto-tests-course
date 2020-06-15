from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector('#treasure')
    x_element = x_element.get_attribute("valuex")
    x = x_element
    y = calc(x)

    input1 = browser.find_element_by_css_selector('#answer')
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