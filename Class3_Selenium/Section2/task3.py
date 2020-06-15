from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = 'http://suninjuly.github.io/selects2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_css_selector('#num1')
    x = x.text
    y = browser.find_element_by_css_selector('#num2')
    y = y.text
    z = int(x) + int(y)# Посчитали числа
    number = str(z)#Перевели в строковый вид

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(number)

    button = browser.find_element_by_css_selector('.btn-default')
    button.click()

finally:
    time.sleep(10)
    browser.quit()