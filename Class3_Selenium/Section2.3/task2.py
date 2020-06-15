from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    submit = browser.find_element_by_css_selector('.btn.btn-primary')
    submit.click()

    new_window = browser.window_handles[1]
    browser.switch_to_window(new_window)

    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_css_selector('#answer')
    input1.click()
    input1.send_keys(y)

    submit2 = browser.find_element_by_css_selector('.btn.btn-primary')
    submit2.click()

finally:
    time.sleep(15)
    browser.quit()