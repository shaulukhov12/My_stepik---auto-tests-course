from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_css_selector('#answer')
    browser.execute_script("window.scrollBy(0, 100);", input1)
    input1.click()
    input1.send_keys(y)

    checkbox = browser.find_element_by_css_selector('#robotCheckbox')
    checkbox.click()

    button1 = browser.find_element_by_css_selector('#robotsRule')
    button1.click()

    submit = browser.find_element_by_css_selector('.btn.btn-primary')
    submit.click()

finally:
    time.sleep(15)
    browser.quit()